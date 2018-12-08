from django.db import models


# Create your models here.
from userinfo.models import UserInfo


class Topic(models.Model):
    name = models.CharField(max_length=50)


class Recommend(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    num = models.SmallIntegerField()


class RecommendList(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    recommend = models.ManyToManyField(Recommend)


class UserTopic(models.Model):
    userid = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    topic_list = models.ManyToManyField(Topic)
