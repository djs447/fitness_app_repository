
from django.contrib.gis import serializers
from rest_framework import serializers
from notifications.models import InboxMessage

class InboxMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InboxMessage
        fields = '__all__'