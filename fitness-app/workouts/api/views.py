from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from workouts.api.serializers import WorkoutSerializer, WorkoutSampleSerializer
from workouts.api.permissions import IsOwnerOrReadOnly
from workouts.models import Workout, WorkoutSample


class WorkoutPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

class WorkoutViewSet(viewsets.ModelViewSet):

    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
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


class WorkoutSampleViewSet(viewsets.ModelViewSet):

    queryset = WorkoutSample.objects.all()
    serializer_class = WorkoutSampleSerializer
    permission_classes = []
