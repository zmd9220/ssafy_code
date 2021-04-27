from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    # new를 빼버리고 create에서 두가지 기능을 통합
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    # 해당 특정경로를 지정하지 않음
    path('<int:pk>/', views.detail, name='detail'),
    
    path('<int:pk>/update/', views.update, name='update'),
    
]
