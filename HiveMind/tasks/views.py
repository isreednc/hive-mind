from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.http import JsonResponse, HttpResponse
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token

from .models import Note, Reply
from .utils import *
import json

# NOTE: group == project

@csrf_exempt
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

@csrf_exempt
def get_task_page(request, group_name):
    return redirect('taskboard', group_name)

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
        
# def create_group(request):
#     user = request.user
#     if request.method == 'POST':
#         group_name = request.POST.get('name')  # Or use request.POST['name']
#         if group_name:
#             Group.objects.create(name=group_name)
#             Group.user_set.add(user)

#             HttpResponse(f'Project {group_name} created successfully!')
#             return redirect('project_page', user_id=user.id)
#         else:
#             return HttpResponse('No project name provided.', status=400)
#     return HttpResponse('Invalid request method.', status=405)

# Had to use chatgpt cause im dumb
@csrf_exempt
@login_required  # Ensure only authenticated users can access this view
def create_group(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            # Ensure the CSRF token is valid
            # csrf_token = request.headers.get('X-CSRFToken')
            # if csrf_token != get_token(request):  # Validate CSRF token
            #     return JsonResponse({"message": "CSRF token is missing or incorrect."}, status=403)

            # Parse JSON data from the request body
            data = json.loads(request.body.decode('utf-8'))
            group_name = data.get('name')

            if not group_name:
                return JsonResponse({"message": "Group name is required."}, status=400)

            # Create the new group
            group = Group.objects.create(name=group_name)

            # Add the current user to the newly created group
            group.user_set.add(request.user)

            return JsonResponse({"message": "Group created successfully and you were added to it!"}, status=200)
            # return redirect('project_page', user_id=request.user.id)

        except Exception as e:
            return JsonResponse({"message": f"Error: {str(e)}"}, status=500)

    # If the request is not a POST with fetch (AJAX), return an error
    return JsonResponse({"message": "Invalid request method."}, status=405)