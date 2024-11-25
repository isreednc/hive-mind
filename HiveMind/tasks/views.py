from django.shortcuts import render
from django.contrib.auth.models import Group

from .models import Note, Reply
from .utils import *

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