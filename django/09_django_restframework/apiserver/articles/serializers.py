from rest_framework import serializers
from .models import Article

# QuerySet -> ??? -> JSON Response
# 리스트를 불러올 때 사용하는 시리얼라이저
class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'created_at')

# 상세 페이지
class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
