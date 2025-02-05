from django.urls import path
from .views import projects, project
from . import views

urlpatterns= [
    path('', views.projects, name="projects"),
    path('project/<str:pk>', views.project, name="project"),

    path('create-project/', views.createProject, name="create-project"),
]