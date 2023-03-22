from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from lesson.models import *
from lesson.serializers import *
from rest_framework.permissions import IsAuthenticated
from account.permission import PermissionMixin

class LessonViewSet(PermissionMixin, ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer