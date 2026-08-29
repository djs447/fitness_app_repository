from django.shortcuts import render
from rest_framework import viewsets
from users.api.serializers import ProfileSerializer
from users.models import Profile

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = []
