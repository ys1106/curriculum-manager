from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from userinfo.forms import LoginForm, SignupFrom
from userinfo.models import UserInfo


def login_page(request):  # 로그인
    if request.user.is_authenticated:  # 이미 로그인되어 있다면
        return redirect(reverse('index'))  # index 페이지로

    if request.method == 'POST':  # post방식이면
        form = LoginForm(request.POST)  # 로그인 폼
        if form.is_valid():  # 유효성 검사
            user_id = form.cleaned_data.get('username')  # 입력받은 아이디 저장
            user_password = form.cleaned_data.get('password')  # 입력받은 비밀번호 저장
            
            try:  # 사용자가 입력한 아이디를 가진 사용자가 있는지 확인
                User.objects.get(username=user_id)
            except:  # 없으면 해당 아이디를 가진 사용자가 없다는 에러메시지 출력
                err = '아이디 또는 비밀번호를 다시 확인하세요.'
                return render(request, 'registration/login.html', locals())

            login_user = authenticate(username=user_id, password=user_password)  # 로그인하려는 이용자 찾아서 저장
            
            if login_user is not None: # id와 password를 설정한 login_user가 있으면
                login(request, login_user)  # 로그인 기능 실행
                return redirect(reverse('index'))
            else:  # 없으면 에러메시지
                err = '아이디 또는 비밀번호를 다시 확인하세요.'
        return render(request, 'registration/login.html', locals())
    form = LoginForm()

    return render(request, 'registration/login.html', locals())


def signup_page(request):  # 회원가입
    if request.user.is_authenticated:  # 로그인이 되어 있으면
        return redirect(reverse('index'))  # index 페이지로

    if request.method == 'POST':  # POST 방식이면
        form = SignupFrom(request.POST)  # 회원가입 폼
        if form.is_valid():  # form의 유효성 검증
            try:
                user_password = form.password_check()  # psssword에 password_check 함수의 리턴값 저장
            except:  # password_check에서 에러가 발생하면
                err = '두 비밀번호가 다릅니다.'  # 에러메시지
                return render(request, 'registration/signup.html', locals())  # 회원가입 페이지로
            
            user_id = form.cleaned_data.get('username')  # user_id에 폼에서 username으로 받은 값 저장
            try:
                User.objects.get(username=user_id)  # 아이디로 입력받은 값이 이미 있는 값이라면
                err = '있는 아이디입니다 ^___^'  # 에러메시지
                return render(request, 'registration/signup.html', locals())  # 회원가입 페이지로
            except:  # 입력받은 아이디의 사용자가 없으면
                pass  # 넘어감

            user_name = form.cleaned_data.get('name')  # 폼에서 입력받은 이름 저장
            user_email = form.cleaned_data.get('email')  # 폼에서 입력받은 이메일 저장
            user_birth = form.cleaned_data.get('birth')  # 폼에서 입력받은 생년월일 저장

            try:  # 입력받은 아이디와 이메일을 가지는 유저 생성
                signup_user = User.objects.create_user(username=user_id, email=user_email, password=user_password)
                return redirect(reverse('index'))
            except:  # 해당 유저가 없으면
                return render(request, 'registration/signup.html', locals())

            signup_user.save()  # 회원가입한 유저 정보 저장
            info_user = UserInfo.objects.create(user=signup_user, name=user_name, birth=user_birth)
            info_user.save()  # 유저 정보 UserInfo 데이터베이스에 저장

        err = '회원가입이 실패했습니다.'  # 유효성 검사 실패
        return render(request, 'registration/signup.html', locals())

    form = SignupFrom()
    return render(request, 'registration/signup.html', locals())


def logout_page(request):  # 로그아웃
    logout(request)  # 로그아웃 함수 실행
    return redirect(reverse('index'))
