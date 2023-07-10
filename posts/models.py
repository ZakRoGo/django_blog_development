from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(null=True)
    image = models.ImageField(upload_to="images/", null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="author"
    )

    def __str__(self):
        return f"{self.id}: {self.title}"
