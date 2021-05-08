from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Movie, Genre
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import random 


# Create your views here.
@require_GET
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_GET
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


@require_GET
def recommended(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    genre_list = movie.genres.all() # 정참조. 영화에 해당하는 장르 목록 가져오기.

    g_list = []
    for g in genre_list:
        g_list.append(g.pk)
    
    pick_genre = random.sample(g_list, 1)
    
    genre = get_object_or_404(Genre, pk=pick_genre[0])
    movie_list = genre.movie_set.all().order_by('?')[:10] # 역참조. 10개만 가져오기.

    response_data = serializers.serialize('json', movie_list)
    return HttpResponse(response_data, status=200)
    