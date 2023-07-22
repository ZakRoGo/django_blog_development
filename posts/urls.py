from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [path("<int:pk>/", views.post_delete, name="post_delete")]
