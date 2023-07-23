from django.db.models.fields import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["image", "title", "description"]


class NewsContentForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["date", "author"]
