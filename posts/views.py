from django.contrib.auth.views import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, User
from .forms import NewsContentForm


# Create your views here.
def post_page(request):
    return render(request, "posts_app/post.html", {"posts": Post.objects.all()})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "posts_app/post_detail.html", {"post": post})


@login_required
def add_post(request):
    form = NewsContentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect("post")
    return render(request, "posts_app/add_post.html", locals())


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("post")
    return render(request, "posts_app/post_delete.html", {"post": post})
