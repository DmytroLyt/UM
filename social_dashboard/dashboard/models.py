from django.contrib.auth.models import User
from django.db import models


class SocialMediaAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform_name = models.CharField(max_length=50)
    platform_user_id = models.CharField(max_length=100)


class Message(models.Model):
    account = models.ForeignKey(SocialMediaAccount, on_delete=models.CASCADE)
    content = models.TextField()
    posted_at = models.DateTimeField()
