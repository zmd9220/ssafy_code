from django.shortcuts import render
from .models import Article

# Create your views here.


def edit(request, pk):
    '''
    글을 수정하는 템플릿을 랜더하는 함수
    '''
    article = Article.objects.get(pk=pk)