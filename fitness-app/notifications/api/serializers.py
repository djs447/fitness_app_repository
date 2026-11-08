from notifications.models import InboxMessage
from rest_framework import serializers
from users.api.serializers import UserSerializer


class InboxMessageSerializer(serializers.ModelSerializer):

    sent_by = UserSerializer(read_only=True)

    class Meta:
        model = InboxMessage
        fields = "__all__"
