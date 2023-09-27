from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Post, Topic
from .forms import PostForm

# from django.http import HttpResponse


def home(request):
    query_param = (
        request.GET.get("q") if request.GET.get("q") is not None else ""
    )
    posts = Post.objects.filter(
        Q(topic__title__icontains=query_param)
        | Q(title__icontains=query_param)
        | Q(content__icontains=query_param)
    )
    topics = Topic.objects.all()
    posts_count = posts.count()

    context = {
        "posts": posts,
        "topics": topics,
        "posts_count": posts_count,
    }
    return render(request, "main_app/home.html", context)


def about(request):
    return render(request, "main_app/about.html")


def post(request, post_id):
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
