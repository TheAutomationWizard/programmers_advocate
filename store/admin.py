from django.contrib import admin
from .models import Courses


# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'price', 'discount', 'category', 'last_updated', 'is_available')
    prepopulated_fields = {'slug': ('course_name',)}


admin.site.register(Courses, CourseAdmin)
