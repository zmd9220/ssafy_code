from rest_framework import serializers
from .models import Movie, Review, Comment


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('pk', 'content',)

class ReviewSerializer(serializers.ModelSerializer):

    # comment_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    comment_set = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)
        
class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'title', 'rank',)
        


