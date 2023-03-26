from django.db import models

from course.models import Course


class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Lesson name')
    description = models.TextField(verbose_name='Lesson Description')
    topic = models.TextField(verbose_name='topic')
    code = models.TextField(verbose_name='code')
    file = models.FileField(upload_to='lessonfile/', verbose_name='File with code')
    video = models.FileField(blank=True, upload_to='videolesson/', verbose_name='Video')

    def __str__(self):
        return f'{self.name}'

