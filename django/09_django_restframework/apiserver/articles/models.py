from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # article.comment_set - 다른거 쓰고싶으면 밑에 article에 related_name 추가 

# comment.article
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # related_name='comments'
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)