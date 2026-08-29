from django.shortcuts import render
from rest_framework import viewsets
from workouts.api.serializers import WorkoutSerializer, WorkoutSampleSerializer
from workouts.models import Workout, WorkoutSample

class WorkoutViewSet(viewsets.ModelViewSet):

    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = []

class WorkoutSampleViewSet(viewsets.ModelViewSet):

    queryset = WorkoutSample.objects.all()
    serializer_class = WorkoutSampleSerializer
    permission_classes = []
