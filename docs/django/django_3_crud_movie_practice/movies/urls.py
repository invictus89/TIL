from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/delete/', views.delete, name="delete"),
    path('<int:movie_pk>/scores/', views.create, name="create"),
    path('<int:movie_pk>/scores/<int:score_pk>/', views.delete, name='delete'),
    path('<int:movie_pk>/update/', views.update, name='update'),
]
