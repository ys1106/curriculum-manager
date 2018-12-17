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
        min_length=5,
        label='비밀번호',
        widget=forms.PasswordInput({
            'placeholder': '비밀번호를 입력해주세요'
        })
    )


class SignupFrom(forms.Form):
    username_validator = UnicodeUsernameValidator()

    username = forms.CharField(
        max_length=150,
        label='아이디',
        help_text='150자 이하의 문자나 숫자, 그리고 @/./+/-/_ 만 가능합니다.',
    )
    name = forms.CharField(
        max_length=15,
        label='이름'
    )
    email = forms.EmailField()
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

    def password_check(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password+mismatch',
            )
        return password2


