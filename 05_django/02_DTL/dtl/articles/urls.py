# articles/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views

# 변수명 app_name은 꼭 지켜야 한다.
app_name = 'articles'


urlpatterns = [
    # URL mapping -> include
    # Naming URL patterns
    path('index/', views.index, name='index'),

    # http://127.0.0.1:8000/articles/create/
    path('create/', views.create, name='create'),
    path('<name>/profile', views.profile, name='create'),
    path('<int:age>/', views.info, name='info'),   
]