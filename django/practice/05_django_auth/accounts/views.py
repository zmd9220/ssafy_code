from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login 
from django.contrib.auth import logout as auth_logout 
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm
# Create your views here.


def index(request):
    # user list 뽑아서 index.html에 전달
    users = get_user_model().objects.all()
    context = {
        'users': users,
    }
    return render(request, 'accounts/index.html', context)



@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    
    if request.method == 'POST': # 회원 가입 반영
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 로그인까지 시켜주기
            auth_login(request, user)
            # login_required 에 의해 넘겨져 온 경우 next 인자를 확인 후 다시 원래 위치로 돌리기
            # return redirect(request.GET.get('next') or 'accounts:index')
            return redirect('accounts:index')

    else: # 회원 가입 폼 넘겨주기
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/forms.html', context)

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')

    if request.method == 'POST': # 로그인 프로세스
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else: # id 비밀번호 입력 폼 제공
        form = AuthenticationForm(request)
    context = {
        'form': form,
    }
    return render(request, 'accounts/forms.html', context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('accounts:index')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if not request.user.is_authenticated:
        return redirect('accounts:index')
    
    if request.method == 'POST': # 정보
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else: # 정보 수정 폼 제공
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/forms.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        # 순서를 꼭 삭제 후 로그아웃으로 진행 (로그아웃 먼저 진행시 request 객체 값이 사라짐)
        request.user.delete()
        auth_logout(request)
    return redirect('accounts:index')


@login_required
@require_http_methods(['GET', 'POST'])
def password(request):
    if not request.user.is_authenticated:
        return redirect('accounts:index')
    
    if request.method == 'POST': # 비밀 번호 변경 반영
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # 로그인 상태 유지(새로운 세션 발급)
            update_session_auth_hash(request, request.user)
            return redirect('accounts:index')
    else:  # 비밀번호 변경 폼 제공
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/password.html', context)
