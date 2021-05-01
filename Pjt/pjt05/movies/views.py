from django.shortcuts import render,redirect,get_object_or_404
from .models import Movie
from .forms import MovieForm
from django.views.decorators.http import require_GET, require_http_methods, require_POST

@require_GET
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
    }
    return render(request,'movies/index.html',context)

@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
    context = {
        'form':form,
    }
    return render(request,'movies/create.html',context)

@require_GET
def detail(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    context = {
        'movie':movie,
    }
    return render(request, 'movies/detail.html', context)

@require_POST
def delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('movies:index')

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/update.html', context)