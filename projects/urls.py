from django.urls import path
from .views import projects, project
from . import views

urlpatterns= [
    path('', views.projects, name="projects"),
    path('project/<str:pk>', views.project, name="project"),

    path('create-project/', views.createProject, name="create-project"),
    # This is where we are going to pass the primary key of the project we want to update and
    # how the system will know which project to update
    path('update-project/<str:pk>', views.updateProject, name="update-project"),

    path('delete-project/<str:pk>', views.deleteProject, name="delete-project"),
]