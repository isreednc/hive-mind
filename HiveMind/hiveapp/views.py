from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, models
from django.contrib import messages

from tasks.utils import *
from .models import Timeline_Node

# Create your views here.
def index(request):
    return render(request, 'homepage.html')

@login_required
def projectsPage(request):
    current_user_id = request.user.id
    return redirect('project_page', user_id=current_user_id)
    

@login_required
def timelinePage(request, group_name):
    if (request.method != "GET"):
        pass

    user = request.user;
    if validate_user_group(user, group_name) == False:
        return redirect('home')
    
    current_group = Group.objects.get(name=group_name)
    timeline_nodes = Timeline_Node.objects.filter(group=current_group)

    return render(request, 'hiveapp/timeline.html', {
        'user': user,
        'group': current_group,
        'timeline_nodes': timeline_nodes,
    })

def updatesPage(request):
    return render(request, 'hiveapp/updates.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
            
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("Login failed."))
            return redirect('login')
    else:
        return render(request, 'hiveapp/auth/login.html', {})
