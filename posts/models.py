from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from django.utils.timezone import now


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(default=now, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="author"
    )
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id}: {self.title}"

    def get_absolute_url(self):
        return reverse("post")


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_likes")


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    date = models.DateTimeField(default=now)
    active = models.BooleanField(default=False)

    def __str__(self):
        return "%s - %s" % (self.post.title, self.author)
