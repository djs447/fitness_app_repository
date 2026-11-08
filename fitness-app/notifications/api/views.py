from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import InboxMessage
from .serializers import InboxMessageSerializer


class InboxMessageViewSet(viewsets.ModelViewSet):
    queryset = InboxMessage.objects.all()
    serializer_class = InboxMessageSerializer

    def get_queryset(self):
        if self.action == "list":
            return InboxMessage.objects.filter(user=self.request.user)
        return super().get_queryset()

    @action(
        detail=True, methods=["post"], url_name="mark-as-read", url_path="mark-as-read"
    )
    def mark_as_read(self, request, pk=None):
        message = self.get_object()
        message.read = True
        message.save()
        return Response(self.get_serializer(message).data, status=200)

    @action(detail=True, methods=["delete"], url_name="delete", url_path="delete")
    def delete(self, request, pk=None):
        message = self.get_object()
        message.delete()
        return Response(status=204)
