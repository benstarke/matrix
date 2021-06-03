from django.urls import path
from . import views
from .views import *


app_name = "SHCOOL"

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('Search', views.Search, name='Search'),
    path('About', views.About, name='About'),
    path('Service', views.Service, name='Service'),
    path('Gallary', views.Gallary, name='Gallary'),
    path('', views.OverListView.as_view(), name='OverListView'),
]


