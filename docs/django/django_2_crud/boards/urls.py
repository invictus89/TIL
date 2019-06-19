from django.urls import path
from . import views

app_name = 'boards'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'), # GET: 페이지 요청 / POST: 글 작성
    path('index/<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:board_pk>/update/', views.update, name='update'), # GET: 페이지 요청 / POST : 업데이트
    path('<int:board_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:board_pk>/comments/<int:comment_pk>/delete', views.comments_delete, name='comments_delete'),
]
