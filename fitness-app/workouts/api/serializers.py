from rest_framework import serializers
from workouts.models import Workout, WorkoutSample
from users.api.serializers import WorkoutUserSerializer

class WorkoutSerializer(serializers.ModelSerializer):

    user = WorkoutUserSerializer(read_only=True)

    class Meta:
        model = Workout
        fields = '__all__'
        read_only_fields = ['user']

class WorkoutSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSample
        fields = '__all__'