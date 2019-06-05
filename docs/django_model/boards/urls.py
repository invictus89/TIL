from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('index/<int:pk>/', views.detail),
]
