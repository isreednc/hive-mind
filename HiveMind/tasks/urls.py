from django.urls import path
from . import views

urlpatterns = [
    path('taskboard/<str:group_name>', views.task_page, name='taskboard'),
    path('update-note-position/', views.update_note_position, name='update_note_position'),
    path('taskboard/create-note/<str:group_name>/', views.create_note, name='create_note'),
]