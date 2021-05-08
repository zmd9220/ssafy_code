from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse

@require_GET
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST) 
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)


@require_GET
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.all()
    comment_form = CommentForm()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'community/detail.html', context)


@require_POST
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect('community:detail', review.pk)
    context = {
        'comment_form': comment_form,
        'review': review,
        'comments': review.comment_set.all(),
    }
    return render(request, 'community/detail.html', context)


@require_POST
def like(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user

        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            liked = False
        else:
            review.like_users.add(user)
            liked = True
        response_data = {
            'liked': liked,
            'count': review.like_users.count(),
        }
    #     return redirect('community:index')
        return JsonResponse(response_data)
    # return redirect('accounts:login')
    return HttpResponse(status=401)

# @require_POST
# def likes(request, article_pk):
#     if request.user.is_authenticated:
#         article = get_object_or_404(Article, pk=article_pk)

#         if article.like_users.filter(pk=request.user.pk).exists():
#         # if request.user in article.like_users.all():
#             # 좋아요 취소
#             article.like_users.remove(request.user)
#             liked = False
#         else:
#             # 좋아요 누름
#             article.like_users.add(request.user)
#             liked = True
#         # js 에서 응답 받을 데이터, json으로 보낼 것 받는 곳에서는 response 객체로 받음
#         response_data = {
#             'liked': liked,
#             'count': article.like_users.count(),
#         }
#         return JsonResponse(response_data)
#         # return redirect('articles:index')
#     # return redirect('accounts:login')
#     return HttpResponse(status=401)