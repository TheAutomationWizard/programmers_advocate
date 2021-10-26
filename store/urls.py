from django.urls import path
from . import views

urlpatterns = [
    path('', views.browse, name='courses'),
    path('<slug:category_slug>/', views.all_courses, name='browse_by_category')
]