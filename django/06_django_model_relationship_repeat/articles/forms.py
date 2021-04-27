from django import forms
from .models import Article
from django.contrib.auth import get_user_model

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)
        


