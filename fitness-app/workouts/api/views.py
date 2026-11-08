from django.db import transaction
from django.db.models import Count, Exists, OuterRef
from django.shortcuts import get_object_or_404
from notifications.tasks import (
    send_inbox_message_notification,
    send_workout_congratulations,
)
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.api.serializers import LikeSerializer
from users.models import Like
from workouts.api.permissions import IsOwnerOrReadOnly
from workouts.api.serializers import (
    CommentSerializer,
    WorkoutSampleSerializer,
    WorkoutSerializer,
)
from workouts.models import Comment, Workout, WorkoutSample


class WorkoutPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


class WorkoutViewSet(viewsets.ModelViewSet):

    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = WorkoutPagination

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.annotate(like_count=Count("likes", distinct=True))

        user = self.request.user
        if user.is_authenticated:
            queryset = queryset.annotate(
                is_liked=Exists(
                    Like.objects.filter(
                        workout_id=OuterRef("pk"),
                        user=user,
                    )
                )
            )
        else:
            queryset = queryset.annotate(is_liked=Exists(Like.objects.none()))
        return queryset

    @action(detail=False, methods=["get", "post"])
    def me(self, request):
        if request.method == "GET":
            my_workouts = (
                self.get_queryset()
                .filter(user=request.user)
                .order_by("-started_at", "-id")
            )
            page = self.paginate_queryset(my_workouts)
            serializer = WorkoutSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = WorkoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            serializer.save(user=request.user)
            transaction.on_commit(
                lambda: send_workout_congratulations.delay(serializer.instance.id)
            )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["get", "post"])
    def comments(self, request, pk=None):
        workout = self.get_object()
        if request.method == "GET":
            comments = Comment.objects.filter(workout=workout)
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
        elif request.method == "POST":
            serializer = CommentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user, workout=workout)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(
        detail=True,
        methods=["patch"],
        url_path=r"comments/(?P<comment_id>[^/.]+)",
        url_name="comment-detail",
    )
    def edit_comment(self, request, pk=None, comment_id=None):
        workout = self.get_object()
        comment = get_object_or_404(
            Comment, id=comment_id, workout=workout, user=request.user
        )
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=True,
        methods=["delete", "post"],
        url_path="like",
        url_name="like",
    )
    def like(self, request, pk=None):
        workout = self.get_object()
        if request.method == "DELETE":
            like = get_object_or_404(Like, user=request.user, workout=workout)
            like.delete()
            return Response({"liked": False}, status=status.HTTP_204_NO_CONTENT)
        elif request.method == "POST":
            created = Like.objects.create(user=request.user, workout=workout)
            return Response(
                {"liked": True},
                status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
            )

    @action(
        detail=True,
        methods=["get"],
        url_path="likes",
        url_name="likes",
    )
    def get_likes(self, request, pk=None):
        workout = self.get_object()
        likes = Like.objects.filter(workout=workout)
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)

    @action(
        detail=True,
        methods=["get"],
        url_path="route",
        url_name="route",
    )
    def route(self, request, pk=None):
        workout = self.get_object()
        points = workout.samples.all()
        serializer = WorkoutSampleSerializer(points, many=True)
        return Response(serializer.data)

    @action(
        detail=True,
        methods=["post"],
        url_path="share",
        url_name="share",
    )
    def share(self, request, pk=None):
        sent_by = request.user
        user_ids = request.data.get("user_ids", [])
        [
            send_inbox_message_notification.delay(
                user_id=user_id, workout_id=self.get_object().id, sent_by=sent_by
            )
            for user_id in user_ids
        ]
        return Response({"message": "Inbox message shared successfully"})


class WorkoutSampleViewSet(viewsets.ModelViewSet):

    queryset = WorkoutSample.objects.all()
    serializer_class = WorkoutSampleSerializer
    permission_classes = []


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
