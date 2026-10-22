
from rest_framework import serializers
from users.models import Goal, Profile, User

class ProfileSerializer(serializers.ModelSerializer):

    goals = serializers.SerializerMethodField()
    profile_picture = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def get_goals(self, obj):
        return GoalSerializer(obj.goals.all(), many=True).data

    def validate_profile_picture(self, value):
        #TODO Add more validation (requiest-size limits, image re-encoding / content verification)
        #TODO Add clean-up logic for old profile pictures
        if value is not None and value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError("Profile picture must be less than 5MB.")
        return value

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

class LikeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class LikeWorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = "Workout"
        fields = ['id', 'name']

class LikeSerializer(serializers.ModelSerializer):
    user = LikeUserSerializer(read_only=True)
    workout = LikeWorkoutSerializer(read_only=True)

    class Meta:
        model = "Like"
        fields = '__all__'
        read_only_fields = ['user', 'workout']

