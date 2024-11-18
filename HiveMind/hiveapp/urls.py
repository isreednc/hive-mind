from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("/", views.index, name="home"),
    # path("login/", views.login, name="login"),
    path("projects/", views.projectsPage, name="projects"),
    path('timeline/', views.timelinePage, name='timeline'),
    path('updates/', views.updatesPage, name='updates')
]