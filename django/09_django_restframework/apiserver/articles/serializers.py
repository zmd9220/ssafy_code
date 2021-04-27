from rest_framework import serializers
from .models import Article, Comment

# QuerySet -> ??? -> JSON Response
# 리스트를 불러올 때 사용하는 시리얼라이저
class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'created_at')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        # # articles 항목은 읽을 때만 사용 - 유효성 검사를 하지 않는다. 
        # -> content만 보내도 유효성 검사 통과 가능
        read_only_fields = ('article',)


# 상세 페이지
class ArticleSerializer(serializers.ModelSerializer):
    # 역참조 필드의 pk 목록에 대한 필드
    # comment_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True) 
    # 글의 상세 페이지에서 글의 댓글까지 모두 불러올 것 - 
    # 읽을때만 가지고 올것(read_only) + 유효성 검사를 하지않도록 - GET, 여러 개를 가져옴 (many=True)
    comment_set = CommentSerializer(many=True, read_only=True) # 사용할거면 commentserializer를 이 클래스보다 위에 둬야함(먼저 읽도록)
    # 장고 queryset api를 이용한 source를 기반으로 데이터 정수값을 반환받아 현재 댓글의 갯수를 출력
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'