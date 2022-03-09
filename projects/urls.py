from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('submit/',views.submit_project,name='submit'),
    path('browse/',views.browse,name='browse'),
    path('projects/<int:pk>/',views.project_detail,name='project_detail'),
]