from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    birth = models.DateField()
