from django import forms
from .models import Community_Review, Community_Comment

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Community_Review
        fields = ('title', 'movie_title', 'rank', 'content')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Community_Comment
        fields = ('content',)