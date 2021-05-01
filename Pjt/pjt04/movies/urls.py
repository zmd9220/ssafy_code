
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # 전체 영화 목록 조회 페이지
    path('', views.index, name='index'),
    # 새로운 영화 form 작성 페이지
    path('new/', views.new, name='new'),
    # 영화 데이터 저장 페이지
    path('create/', views.create, name='create'),
    # 영화 상세 페이지
    path('<int:pk>/', views.detail, name='detail'),
    # 영화 수정 데이터 폼 페이지
    path('<int:pk>/edit/', views.edit, name='edit'),
    # 영화 수정을 반영 하는 페이지
    path('<int:pk>/update/', views.update, name='update'),
    # 영화 정보 삭제 페이지
    path('<int:pk>/delete/', views.delete, name='delete'),
]
