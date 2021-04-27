from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
# 밑에 함수 명과 이름이 같으므로 이름을 다르게 해서 가져오기
# from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserChangeForm, CustomUserCreationForm
# Create your views here.


def login(request):
    # 지금 로그인 상태인지 체크 t/f - 로그인 했으면 밑의 부분(로그인하는 부분) 필요없음 다시 돌려보냄
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST': # ID, PWD 확인 후 세션 발급
        form = AuthenticationForm(request, request.POST)
        # Session 발급
        if form.is_valid():
            auth_login(request, form.get_user())
            # 만약 next 파라미터가 있으면 next로 보낸다.
            # 없으면 articles:index로 보낸다.
            return redirect(request.GET.get('next') or 'articles:index')
            # redirect => 주소창에 엔터 => 항상 get 요청
    else: # GET => 로그인 form 제공
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    auth_logout(request)
    return redirect('articles:index')

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST': # 회원가입 후 로그인
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else: # 회원가입 form 제공
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('articles:index')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        # form = UserChangeForm(request.POST)
        form = CustomUserChangeForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def password(request):
    if request.method == 'POST': # 비밀번호 변경 로직
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid(): # 필드 유효성 + 작성한 비밀번호 2개가 일치하는지
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else: # 비밀번호 변경 폼을 넘겨줌
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'accounts/password.html', context)