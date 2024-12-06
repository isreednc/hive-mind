from django.shortcuts import render
from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.utils.timezone import now

from .models import Note, Reply
from .utils import *
import json

# Create your views here.
def task_page(request, group_name):
    if request.method != "GET":
        pass    # TODO
    
    user = request.user
    if validate_user_group(user, group_name) == False:
        # TODO: implement permission_denied.html
        return render(request, 'permission_denied.html')
    
    current_group = Group.objects.get(name=group_name)
    notes = Note.objects.filter(group=current_group)

    return render(request, 'tasks.html', {
        'group': current_group,
        'notes': notes,
        'user': user,
    })    

def update_note_position(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # Parse the JSON data
        note_id = data.get('noteId')
        print(note_id)
        top = data.get('top')
        left = data.get('left')

        # Find the note in the database by ID
        try:
            note = Note.objects.get(id=note_id)
            note.pos_top = top
            note.pos_left = left
            note.save()  # Save the new position to the database

            return JsonResponse({'success': True})
        except Note.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Note not found'})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})

def submit_new_note(request, group_name):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse the JSON data from the request
            content = data.get('note')

            if not content or content.strip() == "":
                return JsonResponse({'error': 'Note content cannot be empty.'}, status=400)

            current_group = Group.objects.get(name=group_name)

            # Create a new note
            note = Note.objects.create(
                content=content,
                user=request.user,
                group=current_group,
                created_at=now()
            )

            return JsonResponse({
                'message': 'Note submitted successfully.',
                'note': {
                    'id': note.id,
                    'content': note.content,
                    'user': note.user.username,
                    'created_at': note.created_at.isoformat(),
                }
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data.'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

def project_page(request, user_id):
    current_user = request.user;
    if (user_id != current_user.id):
        return render(request, 'permission_denied.html')

    user_group_projects = current_user.groups.all();

    return render(request, 'project.html', {
        'projects': user_group_projects,
        'user': current_user,
    })
        