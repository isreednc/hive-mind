from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'homepage.html')

def projectsPage(request):
    return render(request, 'hiveapp/projects.html')

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
