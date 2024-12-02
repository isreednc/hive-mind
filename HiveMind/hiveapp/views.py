from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, models
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'homepage.html')

@login_required
def projectsPage(request):
    current_user = request.user
    user_groups = current_user.groups.all()
    return render(request, 'hiveapp/projects.html', {
        'user': current_user,
        'groups': user_groups,
    })

@login_required
def timelinePage(request):
    return render(request, 'hiveapp/timeline.html')

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
