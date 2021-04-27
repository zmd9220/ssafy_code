
from django.urls import path
from . import views

app_name = 'second'

# ~/second/
urlpatterns = [
    path('introduce/<str:name>/<int:age>/', views.introduce, name='introduce')
]
