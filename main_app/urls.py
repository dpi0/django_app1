from django.urls import path
from .views import (
    home,
    about,
    post,
    create_post,
    update_post,
    delete_post,
    login_view,
    logout_view,
    register_view,
)

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("", home, name="home"),
    path("home/", home, name="home"),
    path("about", about, name="about"),
    path("post/<int:post_id>/", post, name="post"),
    path("create_post/", create_post, name="create_post"),
    path("update_post/<int:post_id>/", update_post, name="update_post"),
    path("delete_post/<int:post_id>/", delete_post, name="delete_post"),
]
