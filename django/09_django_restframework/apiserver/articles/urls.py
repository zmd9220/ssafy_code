from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.articles),
    path('articles/<int:pk>/', views.article_detail),
    path('comments/', views.comments),
    path('comments/<int:pk>/', views.comment_detail),
    # 리소스 계층 구조 articles/1/comments/ - URL로 해당 위치가 어떤 자원을 가지고 어떤 표현을 할지 유추 가능하도록
    path('articles/<int:article_pk>/comments/', views.article_comments),
]