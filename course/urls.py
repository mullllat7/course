from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from course.views import *

router = DefaultRouter()

router.register('course', CourseViewSet)
router.register('review', ReviewViewSet)
router.register('saved', SavedViewSet)
router.register('like', LikeViewSet)
router.register('rating', RatingViewSet)


urlpatterns = [
    path('', include(router.urls)),

]