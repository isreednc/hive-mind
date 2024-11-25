from django.shortcuts import render
from django.contrib.auth.models import Group

from .models import Note, Reply
from .utils import *

# Create your views here.
def task_page(request, group_id):
    if request.method != "GET":
        pass    # TODO
    
    user = request.user
    if validate_user_group(user, group_id) == False:
        # TODO: implement permission_denied.html
        return render(request, 'permission_denied.html')
    
    group = Group.objects.filter(id=group_id)
    group_users = group.user_set.all()
    notes = Note.objects.filter(Group=group)

    return render(request, 'tasks.html', {
        'group': group,
        'users': group_users,
        'notes': notes
    })    