from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm, 
    PasswordChangeForm,
)
from .forms import CustomUserChangeForm, CustomUserCreationForm


# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('articles:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        # form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)


def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        # 팔로우 누르는 유저와 팔로우를 받는 유저를 연결하거나 끊는 기능 - 신청, 끊기
        # 팔로우 될 유저 - 현재 페이지를 통해 보고 있는 유저
        User = get_user_model()
        you = get_object_or_404(User, pk=user_pk)
        # 팔로우 할 유저 - 로그인 한 유저
        me = request.user

        # 나 자신을 팔로우 할 수 없다.
        if you != me:
            # get을 쓰면 객체를 반환하는데, 만약 없는 유저일 경우 에러가 발생
            # filter를 통한 쿼리셋 리턴은 있으면 데이터가 있는 쿼리셋, 없으면 빈 쿼리셋을 반환함
            # 그래서 에러로 부터 안전
            if you.followers.filter(pk=me.pk).exists():
            # if request.user in person.followers.all():
                # 팔로우 끊음
                you.followers.remove(me)
            else:
                # 팔로우 신청
                you.followers.add(me)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')

# 실제 쿼리셋을 만드는 작업에는 DB 작업이 포함되지 않음
q = Entry.objects.filter(headline__startswith="What")
q = q.filter(pub_date__lte=datetime.date.today())
q = q.exclude(body_text__icontains="food")
# 실제 쿼리셋을 db로 보내는 시점은 평가를 할 때
print(q)

# Iteration
# 쿼리셋은 반복 가능하며 처음 반복할 때 데이터베이스 쿼리를 실행(평가)
for e in Entry.objects.all():
    pass

# bool()
if Entry.objects.filter(title__ 'text'):
    pass
