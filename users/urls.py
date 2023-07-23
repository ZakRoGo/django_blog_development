from django.contrib.auth.views import TemplateView
from django.urls import include, path
from . import views


app_name = "users"

urlpatterns = [
    path(
        "login/",
        TemplateView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register_request, name="register"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("profile/<str:username>/", views.profile, name="profile"),
    path("<str:username>/", views.user_profile, name="user_profile"),
]
