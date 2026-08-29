from rest_framework import serializers
from workouts.models import Workout, WorkoutSample

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

class WorkoutSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSample
        fields = '__all__'