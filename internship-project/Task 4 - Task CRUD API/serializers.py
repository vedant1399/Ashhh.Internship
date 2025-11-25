from rest_framework import serializers
from core.models import Task
from django.contrib.auth.models import User
from core.models import Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']

class TaskSerializer(serializers.ModelSerializer):
    assigned_user = UserSerializer(read_only=True)
    assigned_user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='assigned_user', write_only=True, required=False, allow_null=True)
    project_id = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), source='project', write_only=True)
    class Meta:
        model=Task
        fields=['id','project','project_id','title','description','status','due_date','assigned_user','assigned_user_id','created_at']
        read_only_fields=['project','assigned_user','created_at']
