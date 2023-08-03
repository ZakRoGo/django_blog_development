from django.contrib.auth.models import User
from .models import Profile
from posts.models import Post
from django.shortcuts import get_object_or_404, render, redirect
from .forms import RegisterUserForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import UpdateUserForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register_request(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("posts:post")

        messages.error(request, "Unsuccessful registration. Invalid Information.")
    form = RegisterUserForm()
    return render(
        request=request,
        template_name="registration/register.html",
        context={"register_form": form},
    )


def user_profile(request, username):
    u = User.objects.get(username=username)
    p = Post.objects.all().filter(author__username=username)
    return render(request, "users_app/user_profile.html", {"username": u, "posts": p})


@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile is updated successfully")
            return redirect("users:user_profile", profile.user.username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(
        request,
        "users_app/edit_profile.html",
        {"user_form": user_form, "profile_form": profile_form},
    )
