from rest_framework import serializers
from users.api.serializers import CommentUserSerializer, WorkoutUserSerializer
from workouts.models import Comment, Workout, WorkoutSample


class WorkoutSerializer(serializers.ModelSerializer):

    pace = serializers.SerializerMethodField()
    heart_rate = serializers.SerializerMethodField()
    user = WorkoutUserSerializer(read_only=True)
    like_count = serializers.IntegerField(read_only=True)
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Workout
        fields = "__all__"
        read_only_fields = ["user"]

    def get_pace(self, obj):
        return obj.average_pace

    def get_is_liked(self, obj):
        return getattr(obj, "is_liked", False)

    def get_heart_rate(self, obj):
        return obj.heart_rate


class WorkoutSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSample
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):

    user = CommentUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["user"]
