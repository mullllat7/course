from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg
from course.models import Course, Rating


@receiver(post_save, sender=Rating)
def review_created(sender, instance, created, **kwargs):
    rating = Rating.objects.filter(course=instance.course).aggregate(rating=Avg('rating')).get('rating')
    instance.course.rating = rating
    instance.course.save()