from django.contrib.auth.models import User
from .models import Profile
from django.shortcuts import render, redirect
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
            return redirect("post")

        messages.error(request, "Unsuccessful registration. Invalid Information.")
    form = RegisterUserForm()
    return render(
        request=request,
        template_name="registration/register.html",
        context={"register_form": form},
    )


def profile(request):
    return render(request, "profile.html")


def user_profile(request, username):
    u = User.objects.get(username=username)
    return render(request, "user_profile.html", {"username": u})


@login_required
def edit_profile(request):
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile is updated successfully")
            return redirect("profile")
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(
        request,
        "registration/edit_profile.html",
        {"user_form": user_form, "profile_form": profile_form},
    )
