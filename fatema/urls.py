from django.urls import path

from fatema.models import Project
from . import views

urlpatterns = [
    path('clients/', views.clientList, name="clients"),
    path('clientadd/',views.clientAdd, name="clientadd"),
    path('projects/',views.projectlist,name="projectlist"),
    path('update-client/<int:client_id>',views.clientUpdate.as_view()),
   
]
