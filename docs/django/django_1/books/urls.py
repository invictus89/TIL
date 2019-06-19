from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('graduation/', views.graduation),
    path('imagepick/', views.imagepick),
    path('today/', views.today),
    path('ascii-new/', views.asciinew),
    path('ascii-make/', views.asciimake),
    path('original/', views.original),
    path('translated/', views.translated),
]
