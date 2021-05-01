from django.shortcuts import render, redirect, get_object_or_404
from .models import Community_Review, Community_Comment
from .forms import ReviewForm, CommentForm
from django.views.decorators.http import require_http_methods, require_safe
from accounts.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@require_safe
def index(request):
    reviews = Community_Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        user = User(pk=request.user.pk)
        if form.is_valid():
            review = form.save(commit=False)
            review.user_id = user
            review.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    # print(request.user)
    return render(request, 'community/create.html', context)

def detail(request, pk):
    review = get_object_or_404(Community_Review, pk=pk)
    comments = review.comments.all()
    comment_form = CommentForm()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'community/detail.html', context)


def comments_create(request, pk):
    comment_form = CommentForm(request.POST)
    user = User(pk=request.user.pk)
    review = get_object_or_404(Community_Review, pk=pk)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user_id = user
        comment.review_id = review
        comment.save()

        return redirect('community:detail', review.pk)
    context = {
        'comment_form': comment_form,
    }
    return render(request, 'community/detail.html', context)