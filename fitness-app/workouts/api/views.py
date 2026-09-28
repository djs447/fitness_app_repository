from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from workouts.api.serializers import WorkoutSerializer, WorkoutSampleSerializer
from workouts.api.permissions import IsOwnerOrReadOnly
from workouts.models import Workout, WorkoutSample

class WorkoutViewSet(viewsets.ModelViewSet):

    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    @action(detail=False, methods=['get','post'])
    def me(self, request):
        if request.method == 'GET':
            my_workouts = Workout.objects.filter(user=request.user)
            serializer = WorkoutSerializer(my_workouts, many=True)
            return Response(serializer.data)
        serializer = WorkoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class WorkoutSampleViewSet(viewsets.ModelViewSet):

    queryset = WorkoutSample.objects.all()
    serializer_class = WorkoutSampleSerializer
    permission_classes = []
