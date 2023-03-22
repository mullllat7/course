from rest_framework import serializers

from lesson.models import *



class LessonSerializer(serializers.ModelSerializer):
    """
    Usual serializer for Lesson
    """
    class Meta:
        model = Lesson
        fields = '__all__'
