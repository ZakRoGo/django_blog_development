from django.db.models.fields import forms
from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["image", "title", "description"]
        labels = {"image": ""}


class NewsContentForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["date", "author"]
        fields = ["title", "description", "image"]


class CommentForm(forms.ModelForm):
    body = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Comment here",
                "rows": 1,
            }
        ),
    )

    class Meta:
        model = Comment
        fields = ["body"]
