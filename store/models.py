from django.db import models
from category.models import Category


# Create your models here.
class Courses(models.Model):
    # Information related to the course
    course_name = models.CharField(max_length=200, primary_key=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    images = models.ImageField(upload_to='photos/course/videos')
    price = models.IntegerField()
    discount = models.IntegerField(blank=True)

    # Non-Primary Product Info
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # Product Additional Information
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.course_name
