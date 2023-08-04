from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.post_page, name="post"),
    path("delete/<int:pk>/", views.post_delete, name="post_delete"),
    path("update/<int:pk>/", views.update_post, name="update_post"),
    path("detail/<int:pk>/", views.post_detail, name="post_detail"),
    path("create/", views.add_post, name="add_post"),
    path("<post_id>/like", views.like, name="like"),
    path("comment/delete/<comment_id>", views.delete_comment, name="delete_comment"),
]
