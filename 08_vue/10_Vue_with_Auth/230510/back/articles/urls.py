from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('articles/',views.article_list),
    path('articles/<int:article_pk>/',views.article_detail),
    path('articles/<int:article_pk>/comments',views.comments_list),
    path('comments/<int:comment_pk>/',views.comment_detail),
]
