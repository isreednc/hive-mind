from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'homepage.html')

def projectsPage(request):
    return render(request, 'hiveapp/projects.html')

def timelinePage(request):
    return render(request, 'hiveapp/timeline.html')

def updatesPage(request):
    return render(request, 'hiveapp/updates.html')
