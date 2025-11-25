from rest_framework import viewsets, permissions
from core.models import Project
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user).order_by('-created_at')
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
