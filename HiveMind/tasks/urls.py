from django.urls import path
from . import views

urlpatterns = [
    path('taskboard/<str:group_name>', views.task_page, name='taskboard'),
    path('update-note-position/', views.update_note_position, name='update_note_position'),
    path('submit-note/<str:group_name>/', views.submit_new_note, name='submit-new-note'),

    path('projects/<int:user_id>/', views.project_page, name='project_page'),
]