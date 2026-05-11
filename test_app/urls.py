from django.urls import path
from test_app import views

urlpatterns = [
    path('home', views.home, name='home'),
]