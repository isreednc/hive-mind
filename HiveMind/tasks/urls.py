from django.urls import path
from . import views

urlpatterns = [
    path('taskboard/<str:group_name>', views.task_page, name='taskboard'),
    path('update-note-position/', views.update_note_position, name='update_note_position'),
    path('submit-note/<str:group_name>/', views.submit_new_note, name='submit-new-note'),

    path('projects/<int:user_id>/', views.project_page, name='project_page'),
    path('create-group/', views.create_group, name='create-group'),
    path('delete-project/<int:project_id>/', views.delete_project, name='delete-group'),

    path('get-task-page/<str:group_name>', views.get_task_page, name='get_task_page'),

    path('timeline/<int:user_id>/', views.timeline_page, name='timeline_page'),
]