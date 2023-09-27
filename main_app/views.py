from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# from django.http import HttpResponse


# temp_db = [
#     {"post_id": 1, "title": "post 1", "content": "content 1"},
#     {"post_id": 2, "title": "post 2", "content": "content 2"},
#     {"post_id": 3, "title": "post 3", "content": "content 3"},
#     {"post_id": 4, "title": "post 4", "content": "content 4"},
# ]


def home(request):
    posts_db = Post.objects.all()
    context = {"posts": posts_db}
    return render(request, "main_app/home.html", context)


def about(request):
    return render(request, "main_app/about.html")


def post(request, post_id):
    # post = None
    # for temp_post in temp_db:
    #     if temp_post["post_id"] == post_id:
    #         post = temp_post

    post = Post.objects.get(id=post_id)
    context = {"post": post}
    # value we get from <int:post_id> is passed to
    # this function, and we can pass on this value to the template
    # using "context" which should be a dict
    return render(request, "main_app/post.html", context)


def create_post(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "main_app/post_form.html", context)


def update_post(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(instance=post)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "main_app/post_form.html", context)


def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        post.delete()
        return redirect("home")

    context = {"obj": post}
    return render(request, "main_app/delete.html", context)
