from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

def index(request):
    # id가 오름차순
    # articles = Article.objects.all()
    # pk를 기준으로 역순으로
    articles = Article.objects.order_by('-pk') 
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def create(request):
    # GET - 빈 Form 렌더링
    if request.method == 'GET':
        form = ArticleForm()
    # POST - 생성로직, 실패시 작성한 Form 렌더링
    else:
        # instance 지정없는 form 안의 모델은 pk = None 형태 그래서 save시 새로운 pk가 부여되고 저장
        # Form에서 instance를 따로 주지 않고 save하면 pk가 자동생성되어서 저장된다는 건가요? ㅇㅇ
        # 새 인스턴스 만들어서 생성하는것과 같다 article = Article() article.save
        form = ArticleForm(request.POST)
        # 데이터가 유효한 경우 => 생성 후 redirect
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
    # get 요청이거나, 데이터가 유효하지 않은 경우
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

# def create(request):
#     if request.method == 'GET':
#         # 비어 있는 폼 데이터
#         form = ArticleForm()
#         # 중복 제거 가능(밑에 있음)
#         # context = {
#         #     'form': form,
#         # }
#         # return render(request, 'articles/create.html', context)
#     else: # POST
#         # 장고 form 생성 이후에는 편하게 사용가능
#         form = ArticleForm(request.POST) # POST로 사용자가 보낸 데이터를 일단 몽땅 받아옴
#         # 유효성 검사 is_valid = true/false
#         # 성공 케이스
#         if form.is_valid():
#             # 유효성 검사에서 통과하면 해당 데이터 저장 - 이미 폼에서 연결된 모델이 무엇인지 알기 때문에 바로 해당 db 구조에 맞는지 확인 가능
#             form.save()
#             # 유효한 경우에만 인덱스로 돌아가기
#             return redirect('articles:index')

#     # 유효성 검사에서 실패했다고 모든 데이터 날린채 응 돌아가 하면 사용자입장에서 열받음(기껏 열심히 쓴건데 데이터 다날아가니)
#     # 그래서 form에 데이터를 가진채로 다시 돌려서 보내줌 - 그럼 다시 생성화면에 기존 데이터를 가진채 뒤로가기 됨
#     # 위의 get요청과 연동한다면
#     context = {
#         # 사용자가 잘못 입력한 데이터 또는 새 입력 폼
#         'form': form,
#     }
#     # 잘못 입력된 데이터를 가지고 다시 생성 페이지에 돌아감
#     return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    # GET => 수정 페이지 렌더링
    # 단순히 객체 확인이라고 생각해서 필요없다고 느낄수도 있지만
    # 실제 데이터있는지 존재여부(articles에 있는지) 검사도 겸함 - 잘못된 접근시 404를 주기 위해
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        # 현재 가진 form 형식에 맞춰 article로 찾아낸걸 인스턴스로 넣어주기
        # 기존에 알고 있는 정보를 가진 form을 사용자에게 넘겨줘야 하기때문에
        form = ArticleForm(instance=article)

    # POST => 유효성 검사 후 수정 db에 반영
    else:
        # 데이터를 받되 지금 article 인스턴스를 수정하기 위한 폼이다라는 것을 명시
        # 안그러면 새로운 인스턴스로 인식하게됨(새로운 행을 만들게됨) - create와 같은 기능이 됨
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    context = {
    # form만 넘기면 article의 요소들을 form에서 꺼내서 사용은 불가
    'article': article,
    'form': form,
    }
    return render(request, 'articles/update.html', context)


# GET => Form을 받아감
# def new(request):
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)

# # POST => Data 생성
# def create(request):
#     if request.method == 'POST':
#         # 기존 방법
#         # title = request.POST.get('title')
#         # content = request.POST.get('content')
#         # article = Article(title=title, content=content)
#         # article.save()

#         # 장고 form 생성 이후에는 편하게 사용가능
#         form = ArticleForm(request.POST) # POST로 사용자가 보낸 데이터를 일단 몽땅 받아옴
#         # 유효성 검사 is_valid = true/false
#         if form.is_valid():
#             # 유효성 검사에서 통과하면 해당 데이터 저장 - 이미 폼에서 연결된 모델이 무엇인지 알기 때문에 바로 해당 db 구조에 맞는지 확인 가능
#             form.save()
#             # 만약 저장하고 디테일 페이지로 넘기려면
#             # article = form.save() # 이렇게 저장한걸 바로 인스턴스로 만들어 사용해도 가능(이미 해당 db 모델로 구조되어 있기 때문)
#             # return redirect('aricles:detail', article.pk)
#     return redirect('articles:index')