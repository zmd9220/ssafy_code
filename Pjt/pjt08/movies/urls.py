from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('movie/', views.movies),
    path('movie/<int:pk>/', views.movie_detail),
    path('movie/<int:pk>/review/', views.reviews),
    path('movie/<int:pk>/review/<int:review_pk>/', views.review_detail),
    path('movie/<int:pk>/review/<int:review_pk>/comment/', views.comments),
    path('movie/<str:movie_title>/', views.search_movie),
]
