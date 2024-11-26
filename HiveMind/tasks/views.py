from django.shortcuts import render
from django.contrib.auth.models import Group
from django.http import JsonResponse

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
        'notes': notes
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