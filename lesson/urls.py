from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from lesson.views import *

router = DefaultRouter()

router.register('', LessonViewSet)

urlpatterns = [
    path('', include(router.urls)),

]