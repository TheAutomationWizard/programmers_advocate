from django.shortcuts import render, get_object_or_404, HttpResponse

from category.models import Category
from store.models import Courses


def browse(request):
    courses = Courses.objects.all().filter(is_available=True)
    context = {
        'courses': courses
    }

    return render(request, 'store.html', context)


# Create your views here.
def all_courses(request, category_slug=None):
    categories = None
    matching_courses = None

    if categories:
        categories = get_object_or_404(Category, slug=category_slug)
        matching_courses = Courses.objects.filter(category=categories, is_available=True)
        course_count = matching_courses.count()
    else:
        matching_courses = Courses.objects.all().filter(is_available=True)
        course_count = matching_courses.count()

    context = {
        'courses': matching_courses,
        'course_count': course_count
    }

    return render(request, 'store.html', context)
