from django.urls import path
from . import views

urlpatterns = [
    path('taskboard/<str:group_name>', views.task_page, name='taskboard'),
]