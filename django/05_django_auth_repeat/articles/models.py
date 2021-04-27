from django.db import models
from django.contrib.auth import get_user_model
# Model에서 UserModel 과 관계를 정의할 경우 settings.AUTH_USER_MODEL 을 써라.
from django.conf import settings

# Create your models here.
class Article(models.Model):
    # user = models.ForeignKey('user_model', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
