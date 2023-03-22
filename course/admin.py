from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Review)
admin.site.register(SavedCourse)
admin.site.register(Like)
admin.site.register(Rating)