from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie

# index.html 로 렌더링
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

# 입력 폼 페이지로 연결
def new(request):
    return render(request, 'movies/new.html')

# 상세 페이지 - pk를 통해 데이터를 가져와서 html 연결후 데이터를 전달해준다.
def detail(request, pk):
    # movie = Movie.objects.get(pk=pk)
    movie = get_object_or_404(Movie, pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)

# form에서 입력받은 데이터를 가져와서 db에 반영 하고 index로 돌아간다.
def create(request):
    # POST 일 때만 처리
    if request.method == 'POST':
        # form에서 보낸 데이터 가져오기
        title = request.POST.get('title')
        overview = request.POST.get('overview')
        poster_path = request.POST.get('poster_path')
        
        # 실제 DB 에 맞는 모델 클래스 생성 후 데이터를 넣고, DB에 반영
        movie = Movie()
        movie.title = title
        movie.overview = overview
        movie.poster_path = poster_path
        movie.save()

    # A. 작업이 끝나면 메인 화면(전체 영화 조회 페이지)으로 돌아가기
    return redirect('movies:index')
    # # B. 작업이 끝나면 상세 페이지로 가기
    # return redirect('movies:detail', movie.pk)

# 수정 폼 입력 페이지
def edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    context = {
        'movie': movie,
    }
    return render(request, 'movies/edit.html', context)

# 수정 db에 반영하는 페이지
def update(request, pk):
    # POST 일 때만 처리
    if request.method == 'POST':
        # form에서 보낸 데이터 가져오기
        title = request.POST.get('title')
        overview = request.POST.get('overview')
        poster_path = request.POST.get('poster_path')
        
        # id가 일치하는 행을 가져와서 그 부분의 정보를 수정 후 반영
        movie = get_object_or_404(Movie, pk=pk)
        movie.title = title
        movie.overview = overview
        movie.poster_path = poster_path
        movie.save()
    # 상세 페이지에서 변경 되었는지 확인하도록, pk 값을 인자로 같이 넘겨줌(db 찾기용)
    return redirect('movies:detail', pk)

# 삭제 페이지
def delete(request, pk):
    # 해당하는 행을 가져와서 삭제
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    # 삭제 후 처음 화면으로 돌아가기
    return redirect('movies:index')