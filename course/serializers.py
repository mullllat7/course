from rest_framework import serializers

from course.models import *
from lesson.serializers import LessonSerializer


#
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['lessons'] = instance.lessons.count()
        representation['likes'] = instance.likes.count()
        representation['saved'] = instance.saveds.count()
        representation['reviews'] = instance.reviews.count()


        return representation


class ReviewSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Review
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Rating
        fields = ('id', 'course', 'rating', 'author')

    def create(self, validated_data):
        request = self.context.get('request')
        rating, _ = Rating.objects.update_or_create(
            author=request.user,
            course=validated_data.get('course'),
            rating=validated_data.get('rating'),
        )
        return rating

class LikeSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Like
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        like, _ = Like.objects.get_or_create(
            user=request.user,
            course=validated_data.get('course'),
        )
        return like

class SavedCourseSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = SavedCourse
        fields = ('user', 'course')

    def create(self, validated_data):
        request = self.context.get('request')
        saved, _ = SavedCourse.objects.get_or_create(
            user=request.user,
            course=validated_data.get('course'),
        )
        return saved


class CourseRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['reviews'] = ReviewSerializer(instance.reviews.all(), many=True).data
        representation['lessons'] = LessonSerializer(instance.lessons.all(), many=True).data
        representation['likes'] = instance.likes.count()
        representation['saved'] = instance.saveds.count()

        return representation

class MyCourseSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = MyCourse
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        my_course, _ = MyCourse.objects.get_or_create(
            author=request.user,
            course=validated_data.get('course'),
        )
        return my_course

class RegisteredCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredCourse
        fields = '__all__'