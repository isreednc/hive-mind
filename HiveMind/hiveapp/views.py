from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import LoginForm

# Create your views here.
def index(request):
    return render(request, 'homepage.html')

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("../home")
    
    else:
        form = LoginForm()

    return render(request, "login.html", {"form":form})
