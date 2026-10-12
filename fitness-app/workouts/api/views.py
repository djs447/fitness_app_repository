from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from workouts.api.serializers import WorkoutSerializer, WorkoutSampleSerializer, CommentSerializer
from workouts.api.permissions import IsOwnerOrReadOnly
from workouts.models import Workout, WorkoutSample, Comment


class WorkoutPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

class WorkoutViewSet(viewsets.ModelViewSet):

    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = WorkoutPagination

    @action(detail=False, methods=['get','post'])
    def me(self, request):
        if request.method == 'GET':
            my_workouts = Workout.objects.filter(user=request.user).order_by('-started_at', '-id')
            page = self.paginate_queryset(my_workouts)
            serializer = WorkoutSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = WorkoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get','post'])
    def comments(self, request, pk=None):
        workout = self.get_object()
        if request.method == 'GET':
            comments = Comment.objects.filter(workout=workout)
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = CommentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user, workout=workout)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(
        detail=True,
        methods=['patch'],
        url_path=r'comments/(?P<comment_id>[^/.]+)',
        url_name='comment-detail',
    )
    def edit_comment(self, request, pk=None, comment_id=None):
        workout = self.get_object()
        comment = get_object_or_404(Comment, id=comment_id, workout=workout, user=request.user)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class WorkoutSampleViewSet(viewsets.ModelViewSet):

    queryset = WorkoutSample.objects.all()
    serializer_class = WorkoutSampleSerializer
    permission_classes = []

class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
