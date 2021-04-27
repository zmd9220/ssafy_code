from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.articles),
    path('articles/<int:pk>/', views.article_detail),
]