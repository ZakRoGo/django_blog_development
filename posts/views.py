from django.contrib.auth.views import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Comment, Likes, Post
from .forms import CommentForm, NewsContentForm, PostForm


# Create your views here.
def home_page(request):
    return render(request, "home.html")


def post_page(request):
    return render(request, "posts_app/post.html", {"posts": Post.objects.all()})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.all().filter(post__pk=pk)
    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        "post": post,
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form,
    }
    return render(request, "posts_app/post_detail.html", context)


@login_required
def add_post(request):
    form = NewsContentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect("posts:post")
    return render(request, "posts_app/add_post.html", locals())


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("posts:post")
    return render(request, "posts_app/post_delete.html", {"post": post})


def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts:post_detail", post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "posts_app/update_post.html", {"form": form})


def like(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)
    current_likes = post.likes
    liked = Likes.objects.filter(user=user, post=post).count()
    if not liked:
        liked = Likes.objects.create(user=user, post=post)
        current_likes += 1
    else:
        liked = Likes.objects.filter(user=user, post=post).delete()
        current_likes -= 1

    post.likes = current_likes
    post.save()
    return HttpResponseRedirect(reverse("posts:post"))
