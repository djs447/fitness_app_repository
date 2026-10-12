
from rest_framework import serializers
from users.models import Goal, Profile, User

class ProfileSerializer(serializers.ModelSerializer):

    goals = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = '__all__'

    def get_goals(self, obj):
        return GoalSerializer(obj.goals.all(), many=True).data

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'
        read_only_fields = ['id', 'completion_date', 'profile']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile']

class CommentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','id']
        #TODO Consider other fields

class WorkoutUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email','first_name','last_name']
        read_only_fields = ['username','email','first_name','last_name']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user

