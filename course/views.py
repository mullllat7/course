from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from course.models import *
from course.serializers import *

from account.permission import PermissionMixin, IsTeacherOrAdminPermission


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


class LargeResultPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 2

class CourseViewSet(PermissionMixin, ModelViewSet):

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = LargeResultPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['name']
    filterset_fields = ['category']
    ordering_fields = '__all__'
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


class MyCourseViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated, IsTeacherOrAdminPermission]
    queryset = MyCourse.objects.all()
    serializer_class = MyCourseSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        queryset = queryset.filter(author=user)
        return queryset

class RegisteredCourseViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset = RegisteredCourse.objects.all()
    serializer_class = RegisteredCourseSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        queryset = queryset.filter(student=user)
        return queryset