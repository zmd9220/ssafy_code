
from django.urls import path
from . import views

app_name = 'articles'


urlpatterns = [
    # ~/articles/ => 목록 페이지
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    # ~/articles/1/ => 디테일 페이지
    path('<int:pk>/', views.detail, name='detail'),

    # ~/articles/delete/1/ => 삭제 페이지
    path('delete/<int:pk>/', views.delete, name='delete'),

    # ~/articles/edit/1/ => 수정 페이지 throw catch
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('update/<int:pk>/', views.update, name='update'),
]
