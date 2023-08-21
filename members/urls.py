from django.urls import path
from . import views

urlpatterns = [
    path('members/safa', views.safa, name='members'),
    path('members/hassan', views.hassan, name='members'),
    path('members/sahar', views.sahar, name='members'),
    path('members/zeynab', views.zeynab, name='members'),
    path('members/sara', views.sara, name='members'),
    path('members/merve', views.merve, name='members'),
    path('members/sanya', views.sanya, name='members'),
    path('members/husna', views.husna, name='members'),
    path('members/hadia', views.hadia, name='members'),
    path('members/ali', views.ali, name='members'),
            
]