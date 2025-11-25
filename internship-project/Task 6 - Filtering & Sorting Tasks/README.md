# Task 6 - Filtering & Sorting Tasks

Example: add DjangoFilterBackend to filter tasks by status and due_date.

Install:
pip install django-filter

Add to settings:
REST_FRAMEWORK = {
  'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

Example view modification:
```
from django_filters.rest_framework import DjangoFilterBackend
class TaskViewSet(...):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'due_date']
```
