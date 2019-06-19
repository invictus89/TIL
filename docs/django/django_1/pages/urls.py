from django.urls import path
from . import views
# Root Urls를 거쳐서 이곳으로 온다.
urlpatterns = [
    # 여기서 실제 view 를 파악한다.
    path('', views.index),
    path('dinner/', views.dinner),
    path('hello/<str:name>/', views.hello),
    path('intro/<name>/<int:age>/', views.introduce),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('area/<int:num>/', views.area),
    path('dtl_example/', views.dtl_example),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('artii/', views.artii),
    path('result/', views.result),
    path('user-new/', views.user_new),
    path('user-create/', views.user_create),
    path('static-example/', views.static_example),
]
