from django.shortcuts import render, redirect

def index(request):
    if request.user.is_authenticated:
        return redirect('projects')
    return redirect('/hiveapp/login')
