from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Post, Topic
from .forms import PostForm
from django.http import HttpResponse


def login_view(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST["username"].lower()
        password = request.POST["password"]
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username or password is incorrect")

    context = {"page": page}

    return render(request, "main_app/login_and_register.html", context)


def logout_view(request):
    logout(request)
    return redirect("login")


def register_view(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(
                request, "An error occurred during registration"
            )

    context = {"form": form}

    return render(request, "main_app/login_and_register.html", context)


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


@login_required(login_url="login")
def create_post(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "main_app/post_form.html", context)


@login_required(login_url="login")
def update_post(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(instance=post)

    if request.user != post.owner:
        return HttpResponse("You are not the owner of this post")

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "main_app/post_form.html", context)


@login_required(login_url="login")
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.user != post.owner:
        return HttpResponse("You are not the owner of this post")

    if request.method == "POST":
        post.delete()
        return redirect("home")

    context = {"obj": post}
    return render(request, "main_app/delete.html", context)
