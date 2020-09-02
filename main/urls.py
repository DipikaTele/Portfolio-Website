from django.urls import path

from main import views

urlpatterns = [
    path('projects', views.Projects, name='projects'),
    path('languages',views.Languages, name = 'languages'),
    path('',views.Index, name = 'index'),
]