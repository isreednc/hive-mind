from django.urls import path
from . import views

urlpatterns = [
    path('taskboard/', views.task_page, name='taskboard'),
]