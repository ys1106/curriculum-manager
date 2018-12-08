from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserInfo(models.Model):
    userid = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30)
    birth = models.DateField()
