from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

# index.html 을 주세요 x
# article 데이터를 주세요 o
# 요청한 곳에 article 데이터만 넘길것 (서버 처럼)
# api로서 데이터만 넘길거면 api_view라는 데코레이터를 사용해야함
# 앞으로 http method 다양하게 받을 수 있는데, api 서버의 뷰 함수를 작성한다고 명시적으로 표시
@api_view(['GET', 'POST']) # view 함수가 api 응답(데이터 직렬화 후 json 응답)을 한다는 표시 + list에 작성된 http 메서드만 받겠다.
def articles(request):
    if request.method == 'GET':
        # 리스트 형으로 받아올 것이므로, 리스트 형태가 아니면 404 에러 - article 목록을 가져온다, 없으면 404
        article_list = get_list_or_404(Article)
        # QuerySet => JSON
        serializer = ArticleListSerializer(article_list, many=True)
        # 이제 까지 render -> 템플릿 보여주기, redirect -> 사용자 redirect
        # 우리가 하고싶은것 - rest_framework에서 지원하는 직렬화 객체를 통해 json으로 응답 
        # - 해당 응답을 위해 미리 구현된 클래스 Response 이용
        return Response(serializer.data)
    else:
        # 데이터를 받아서 유효성 체크후 유효하지 않다면 에러, 유효하다면 저장
        # 과거처럼 request.POST 가 아니라 get, put, delete 등의 요청의 데이터를 받아서 사용할 경우도 있음
        # 그래서 어떤 형식이든 상관없이 모든 데이터를 받기 위해 .data로 받음
        serializer = ArticleSerializer(data=request.data)
        # raise_exception 은 에러 발생시 자동으로 에러 코드를 반환해줌
        if serializer.is_valid(raise_exception=True):
            serializer.save() # db에 저장
            # return Response() # status code 200 리턴
            # https://developer.mozilla.org/ko/docs/Web/HTTP/Status
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 201 리턴
            # 그냥 201이라고 써도 작동은 하지만 굳이 import 해서 쓰는 이유 - 상수를 변수화 하여 어떤 상수가 어떤 기능을 하는지 알아 보기 쉽게 하기 위함 
        # else:
        #     # 어디에서 에러났는지와 에러코드를 같이 보내줌 - 유효성 검사 실패
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, pk):
    # 3가지 기능에서 모두 사용되므로 맨 위에서 불러오기
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # 시리얼라이저 = 해당 모델 시리얼라이저(수정할 데이터 인스턴스, 수정할 내용 데이터)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    else: # Delete
        # 삭제는 시리얼라이저가 필요 X
        article.delete()
        response = {'pk': pk}
        return Response(response, status=status.HTTP_204_NO_CONTENT)


# index 페이지 주세요!
# article이 비었을 때 -> article이 없는 index.html 페이지가 응답 (빈 페이지)
# get_list_or_404를 사용하면 데이터가 없을 때는 빈 페이지가 아닌 404 에러를 표시함 -> 구조상 이상하게 됨
# def index(request):
#     # articles = get_list_or_404(Article)
#     articles = Article.objects.all()
#     context = {
#         'articles': articles
#     }
#     return render(request, 'index.html', context)


@api_view(['GET'])
def comments(request):
    comment_list = get_list_or_404(Comment)
    serializer = CommentSerializer(comment_list, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, pk):
    comment = get_object_or_404(comment, pk=pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    else: # Delete
        comment.delete()
        response = {'pk': pk}
        return Response(response, status=status.HTTP_204_NO_CONTENT)

# 특정 게시글의 댓글 달기, 댓글 확인
@api_view(['GET', 'POST'])
def article_comments(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        # 1:n 모델에서 n 측에서 역참조
        # comment_list = get_list_or_404(Comment, article=article) # 이렇게 해도 됨   
        comment_list = get_list_or_404(Comment.objects.order_by('-pk'), article=article)
        # comment_list = article.comment_set.all()
        serializer = CommentSerializer(comment_list, many=True)
        return Response(serializer.data)
    else: # POST
        '''
        request.data
        {"content": "안녕하세요, 첫번째 댓글"} # article에 대한 정보가 없음
        '''
        serializer = CommentSerializer(data=request.data)
        '''
        is_valid에서 article을 검사하지 않도록
        read_only_fields에 추가함
        '''
        if serializer.is_valid(raise_exception=True):
            # article 필드에 대한 정보가 없으므로 같이 넣어서 저장
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)