from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from course.views import *

router = DefaultRouter()

router.register('course', CourseViewSet)
router.register('review', ReviewViewSet)
router.register('saved', SavedViewSet)
router.register('like', LikeViewSet)
router.register('rating', RatingViewSet)
router.register('my-course', MyCourseViewSet)
router.register('registered-course', RegisteredCourseViewSet)


urlpatterns = [
    path('', include(router.urls)),

]