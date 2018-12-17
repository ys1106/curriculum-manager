from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from userinfo.models import UserInfo


class Topic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Recommend(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=False, null=False)
    num = models.SmallIntegerField()

    def __str__(self):
        return self.topic.name


class RecommendList(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=False, null=False)
    recommend = models.ManyToManyField(Recommend)

    def __str__(self):
        return self.topic.name


class UserTopic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    topic_list = models.ManyToManyField(Topic)

    def __str__(self):
        return self.user.username + '\'s topics'
