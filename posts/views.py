from django.shortcuts import render
from .models import Post


# Create your views here.
def post_page(request):
    return render(request, "post.html", {"posts": Post.objects.all()})
