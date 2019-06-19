from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login#user session 을 만들기 위한 라이브러리
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm, CustomerUserCreationForm
from django.contrib.auth import update_session_auth_hash, get_user_model
    # 세션이 바뀌어도 사용자 인증을 유지시켜준다. 즉, 로그인 정보가 바뀌어도 로그인 유지
from boards.models import Board

def singup(request):
    # GET과 POST 방식으로 나누어야 한다. 회원가입 폼과 실제 로직 처리 부분이 다르기 때문에
    if request.method == 'POST':
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('boards:index')
    else:
        form = CustomerUserCreationForm()
        context = {'form': form, }
    return render(request, 'accounts/auth_form.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user()) # user session create
            return redirect(request.GET.get('next') or 'boards:index')
    else:
        form = AuthenticationForm()

    context = {'form': form, }
    return render(request, 'accounts/login.html', context)
        
def logout(request):
    auth_logout(request)
    return redirect('boards:index')

def delete(request):
    if request.method == 'POST':
        request.user.delete()
    return redirect('boards:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('boards:index')
    else:
        # 이전 정보를 모두 받아와야 하기 때문에서 instace = request.user
        form = CustomUserChangeForm(instance = request.user)
    context = {'form' : form,}
    return render(request, 'accounts/auth_form.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # 인증 세션이 초기화 되는 것을 막음
            return redirect('boards:index')
    else:
        form = PasswordChangeForm(request.user) # request.user 필수
    context = {'form' : form,}
    return render(request, 'accounts/auth_form.html', context)

# instagram 처럼 주소 뒤에 username 으로 바로 접속하기
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {'person': person,}
    return render(request, 'accounts/profile.html', context)