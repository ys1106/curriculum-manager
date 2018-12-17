from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserInfo(models.Model):  # 회원가입한 회원 정보 저장하는 데이터베이스 모델
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # User 정보 저장 (아이디, 비밀번호, 이메일)
    name = models.CharField(max_length=30)  # 이름
    birth = models.DateField()  # 생년월일
