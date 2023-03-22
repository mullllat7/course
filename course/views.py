from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from course.models import *
from course.serializers import *

from account.permission import PermissionMixin


class ReviewViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        queryset = queryset.filter(user=user)
        return queryset

class RatingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class CourseViewSet(PermissionMixin, ModelViewSet):

    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CourseRetrieveSerializer(instance)
        return Response(serializer.data)


class SavedViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset = SavedCourse.objects.all()
    serializer_class = SavedCourseSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        queryset = queryset.filter(user=user)
        return queryset


class LikeViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        queryset = queryset.filter(user=user)
        return queryset
