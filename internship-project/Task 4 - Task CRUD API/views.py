from rest_framework import viewsets, permissions
from core.models import Task
from .serializers import TaskSerializer
from django.db.models import Q

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return (Task.objects.filter(project__owner=user) | Task.objects.filter(assigned_user=user)).distinct().order_by('-created_at')
    def perform_create(self, serializer):
        serializer.save()
