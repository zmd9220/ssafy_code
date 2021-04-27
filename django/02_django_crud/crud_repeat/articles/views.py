from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

# Create your views here.

# Article 목록을 보여주는 페이지
def index(request):

    articles = Article.objects.all() # queryset

    context = {
        'articles':articles,
    }
    return render(request, 'articles/index.html', context)

# Article 생성 폼을 제공하는 페이지 렌더링
def new(request):
    return render(request, 'articles/new.html')

# new/ 에서 받은 form data를 꺼내서,
# 새로운 article을 생성
def create(request):
    if request.method == 'POST':
        # 전달받은 form data를 꺼낸다. 
        # 210311 11시 GET을 POST로 변경
        # title = request.GET.get('title')
        # content = request.GET.get('content')
        title = request.POST.get('title')
        content = request.POST.get('content')

        # 새로운 article data를 생성한다.
        article = Article()
        article.title = title
        article.content = content
        article.save()

    # 마지막 처리
    # 성공 문자 띄워주기, 처음페이지로 돌아가기 등 다양한방법
    # 지금은 인덱스페이지로 돌려보내주는 방법 해보기 redirect
    # 특정 주소로 보내겠다
    # 사용자를 특정위치로 보내준다.
    # 생성완료시 디테일 페이지로 넘겨 확인하도록
    return redirect('articles:detail', article.pk)

# 상세페이지, pk를 가지고 db에서 데이터들을 가져와서 넘겨줘야함
# db에서 값을 가져오는법 - objects.get or objects.filter 
# get은 pk처럼 꼭 값이 1개이고 항상 존재하는 경우 - 없거나 중복이면 에러남
# filter는 그것과 상관없이 일반적인 경우
def detail(request, pk):
    # article = Article.objects.get(pk=pk)
    # get_object_or_404 데이터가 없으면 404_not found를 보여줌
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article':article        
    }

    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    # if문으로 분기를 통해 method == post 요청일때만 삭제하도록함
    # 해당 잘못된 접근은 에러페이지를 띄우거나 그냥 리다이렉션하거나 개발자 자유
    # 관련 에러 던지는걸로는 (http status) 405 method not allowed
    if request.method == 'POST':
        # pk 값으로 article을 찾는다.
        article = get_object_or_404(Article, pk=pk)

        # article을 삭제한다.
        article.delete()

    # 목록 페이지로 연결한다.
    return redirect('articles:index')


def edit(request, pk):

    # pk 값으로 article을 찾는다.
    article = get_object_or_404(Article, pk=pk)

    # context로 article 값을 template에 전달한다.
    context = {
        'article': article,
    }

    # edit.html(게시글 수정 페이지)를 렌더링한다.
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    if request.method == 'POST':
    # pk 값으로 article을 찾는다.
        article = get_object_or_404(Article, pk=pk)

        # 수정할 내용을 request.GET에서 꺼낸다.
        # title = request.GET.get('title')
        # content = request.GET.get('content')
        
        # article에 수정할 내용을 적용하고 저장한다.
        # article.title = title
        article.title = request.POST.get('title')
        # article.content = content
        article.content = request.POST.get('content')
        article.save()

    # Detail 페이지로 이동한다.
    return redirect('articles:detail', pk)