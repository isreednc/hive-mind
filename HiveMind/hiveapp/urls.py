from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("projects/", views.projectsPage, name="projects"),
    path('timeline/', views.timelinePage, name='timeline'),
    path('updates/', views.updatesPage, name='updates'),
    path('login_user', views.login_user, name='login'),
]