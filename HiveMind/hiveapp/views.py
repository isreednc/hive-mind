from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'base/homepage.html')

def projectsPage(request):
    return render(request, 'base/projects.html')

def timelinePage(request):
    return render(request, 'base/timeline.html')

def updatesPage(request):
    return render(request, 'base/updates.html')