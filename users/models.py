from django.contrib.auth.models import AbstractUser, User
from posts.models import Post
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    image = models.ImageField(
        default="images/naruto.jpg", upload_to="images/", null=True
    )
    bio = models.TextField(max_length=500, null=True, blank=True)
    youtube_url = models.CharField(max_length=255, null=True, blank=True)
    tg_url = models.CharField(max_length=255, null=True, blank=True)
    user_posts = models.ForeignKey(
        Post, null=True, on_delete=models.CASCADE, related_name="user_posts"
    )

    def __str__(self):
        return self.user.username
