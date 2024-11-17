from django.shortcuts import render

# Create your views here.
def task_page(request):
    return render(request, 'tasks.html')