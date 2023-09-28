from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Post, Topic
from ..forms import PostForm
from django.http import HttpResponse


@login_required(login_url="login")  # makes sure user is logged in
def create_post(request):
    form = PostForm()
    topics = Topic.objects.all()

    # uses django's built in form

    if request.method == "POST":
        form = PostForm(request.POST)
        # IMP: this section is for when user creates/updates post
        # we are adding a functionality so that while updating/creating post
        # NOTE: HE CAN ADD NEW TOPIC as well!!!!

        topic_title = request.POST.get("topic")
        topic, created = Topic.objects.get_or_create(title=topic_title)

        Post.objects.create(
            owner=request.user,
            topic=topic,
            title=request.POST.get("title"),
            content=request.POST.get("content"),
        )

        # IMP:  end of this logic
        # if form.is_valid():
        #     post = form.save(commit=False)  # doesn't commit here
        #     post.owner = (
        #         request.user
        #     )  # auto adds the current logged in user to the post
        #     form.save()
        return redirect("home")

    context = {"form": form, "topics": topics}
    return render(request, "main_app/post_form.html", context)


@login_required(login_url="login")
def update_post(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(instance=post)
    topics = Topic.objects.all()

    if request.user != post.owner:
        return HttpResponse("You are not the owner of this post")

    if request.method == "POST":
        # IMP: same thing as above being done here
        topic_title = request.POST.get("topic")
        topic, created = Topic.objects.get_or_create(title=topic_title)
        post.topic = topic
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()

        # form = PostForm(request.POST, instance=post)
        # if form.is_valid():
        #     form.save()
        return redirect("home")

    context = {"form": form, "topics": topics}
    # IMP: we pass the context/return the "context" dict BECAUSE
    # IMP: it contains the variables we want to use in the template
    # NOTE: like here, form is being sent to the template
    # NOTE: so in the template i can do {{ form.XXXX }}

    return render(request, "main_app/post_form.html", context)


@login_required(login_url="login")
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.user != post.owner:
        return HttpResponse("You are not the owner of this post")

    if request.method == "POST":
        post.delete()  # deletes the post
        return redirect("home")

    context = {"object_to_be_deleted": post}
    return render(request, "main_app/delete.html", context)
