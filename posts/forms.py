from django.db.models.fields import forms
from .models import Post


class NewsContentForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["date", "author"]
