from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # ~/articles/
    path('', views.index, name='index'),

    # ~/articles/게시물번호/ : 상세 페이지를 랜더
    path('<int:pk>/', views.detail, name='detail'),
]
