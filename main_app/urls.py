from django.urls import path
from .views import (
    home,
    about,
    post,
)
from .views_drivers.views_auth import (
    login_view,
    logout_view,
    register_view,
)
from .views_drivers.views_crud_post import (
    create_post,
    update_post,
    delete_post,
)
from .views_drivers.views_crud_comment import (
    update_comment,
    delete_comment,
)
from .views_drivers.views_user_profile import user_profile, update_user

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("", home, name="home"),
    path("home/", home, name="home"),
    path("about", about, name="about"),
    path("user/<str:username>/", user_profile, name="profile"),
    path("update_user/", update_user, name="update_user"),
    path("post/<int:post_id>/", post, name="post"),
    path("create_post/", create_post, name="create_post"),
    path("update_post/<int:post_id>/", update_post, name="update_post"),
    path("delete_post/<int:post_id>/", delete_post, name="delete_post"),
    path(
        "update_comment/<int:comment_id>/",
        update_comment,
        name="update_comment",
    ),
    path(
        "delete_comment/<int:comment_id>/",
        delete_comment,
        name="delete_comment",
    ),
]
