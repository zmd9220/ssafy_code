
# ~/pages/ 까지 들어온 상태
from django.urls import path
from . import views

app_name = 'pages'

# 아까 원하던 경로들 사용
urlpatterns = [
    # ~/pages/ 로 접속했을 때
    # views.py/index 함수를 통해서 
    # tmplates/index.html 템플릿이 랜더링
    # name='00' 해당 함수 경로의 별명을 지어주면 변수 처럼 사용가능
    path('', views.index, name='index'),

    path('fake-google/', views.fake_google, name='fake-google'),

    path('introduce/<str:name>/<int:age>/', views.introduce, name='introduce'),

    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
]
