from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

User = get_user_model()


class Category(models.Model):
    slug = models.SlugField()

    def __str__(self):
        return self.slug



class Course(models.Model):
    name = models.CharField(max_length=30, verbose_name='Сourse name')
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE, verbose_name='Сourse category')
    course_image = models.ImageField(upload_to='courseimage/', verbose_name='Сourse photo')
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0, blank=True)
    # comment = models.IntegerField(default=0, blank=True, )
    # like = models.IntegerField(default=0, blank=True, )

    def __str__(self):
        return f'Course --> {self.name} '



class Review(models.Model):
    course = models.ForeignKey(Course, related_name='reviews', on_delete=models.CASCADE, verbose_name='Which course is rated')
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE, verbose_name='Rating owner')
    description = models.CharField(max_length=300, blank=True, verbose_name='Comment')



    def __str__(self):
        return f'<<{self.description}>> by user {self.user}'

class Rating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='ratings')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    rating = models.SmallIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])

    def __str__(self):
        return f'{self.product} - {self.star}'

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'


class Like(models.Model):
    course = models.ForeignKey(Course, related_name='likes', on_delete=models.CASCADE, verbose_name='Which course is liked')
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE, verbose_name='Like owner')

    def __str__(self):
        return f'<<{self.course}>> has been liked by <<{self.user}>>'


class SavedCourse(models.Model):
    course = models.ForeignKey(Course, related_name='saveds', on_delete=models.CASCADE, verbose_name='Course to save')
    user = models.ForeignKey(User, related_name='saveds', on_delete=models.CASCADE, verbose_name='User')

    def __str__(self):
        return f"{self.course} --> {self.user}"

class MyCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='my_courses')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_courses')



class RegisteredCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='registered_courses')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registered_courses')

