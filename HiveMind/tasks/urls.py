from django.urls import path
from . import views

urlpatterns = [
    path('taskboard/<str:group_name>', views.task_page, name='taskboard'),
    path('update-note-position/', views.update_note_position, name='update_note_position'),
]