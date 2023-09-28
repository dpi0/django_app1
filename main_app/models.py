from django.db import models

# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

timeNow = timezone.localtime(timezone.now())


class User(AbstractUser):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True)
    about_user = models.TextField(null=True)
    profile_photo = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


def get_time():
    return timezone.localtime(timezone.now())


class Topic(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at", "-created_at"]
        # this sets the ordering in descending, so newest updated on top

    def __str__(self):
        return self.title


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at", "-created_at"]

    def __str__(self):
        # print(self.content)
        # print(type(self.content))
        return self.content
