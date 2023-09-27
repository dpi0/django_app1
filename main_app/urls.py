from django.urls import path
from .views import home, about, post


urlpatterns = [
    path("", home, name="home"),
    path("home", home, name="home"),
    path("about", about, name="about"),
    path("post/<int:post_id>", post, name="post"),
]
