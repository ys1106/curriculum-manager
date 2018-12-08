from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label='아이디',
        widget=forms.TextInput({
            'placeholder': '아이디를 입력해주세요'
        })
    )
    password = forms.CharField(
        max_length=30,
        min_length=10,
        label='비밀번호',
        widget=forms.PasswordInput()
    )

    def check(self):
        User.check_password(self) #??


class SignupFrom(forms.Form):
    username_validator = UnicodeUsernameValidator()

    username = forms.CharField(
        #_('username'),
        max_length=150,
        label='아이디',
        unique=True,
        help_text='150자 이하의 문자나 숫자, 그리고 @/./+/-/_ 만 가능합니다.',
        validators=[username_validator],
        error_messages={
            'unique': "이미 존재하는 아이디입니다.",
        },
    )
    name = forms.CharField(
        max_length=15,
        label='이름'
    )
    email = forms.EmailField(
        #_('email address'),
        blank=True,
        unique=True,
        error_message={
            'unique': '이미 존재하는 이메일입니다.'
        }
    )
    birth = forms.DateField(label='생년월일')
    password1 = forms.CharField(
        label = '비밀번호',
        strip=False,
        widget=forms.PasswordInput,
        help_text='비밀번호는 10자 이상 30자 이하이어야 합니다. 비밀번호는 개인정보와 비슷하거나, 전부 숫자로 할 수 없습니다.'
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        strip=False,
        widget=forms.PasswordInput,
        help_text='위에서 입력한 비밀번호와 동일한 비밀번호를 입력해주세요'
    )

    def save(self, commit=True):
        pass

