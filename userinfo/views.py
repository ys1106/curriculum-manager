from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from userinfo.forms import LoginForm,SignupFrom
from userinfo.models import UserInfo


def login_page(request): #??
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data.get('id')
            password = form.cleaned_data.get('password')
            try:
                login_user = User.objects.get(username=user_id)
            except:
                return render(request, 'registration/login.html', locals())
            login_user = authenticate(username=user_id, password=password)
            if login_user is not None:
                user_info = UserInfo.objects.get(user=login_user)
                login(request, user=login_user)
                return redirect('/')
        return render(request, 'registration/login.html', locals())
    form = LoginForm()
    return render(request, 'registration/login.html', locals())


def signup(request): #??

    if request.method == 'POST':
        form = SignupFrom(request.POST)
        if form.is_valid():
            pass
        return redirect(reverse('index'))
    # else:
    #     form = SignupFrom()
    return render(request, 'registration/signup.html', locals())


def logout_page(request):

    return redirect(reverse('index'))



