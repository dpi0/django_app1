from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Post, Topic, Comment


def home(request):
    query_param = (
        request.GET.get("q") if request.GET.get("q") is not None else ""
    )
    # NOTE: query param has this condition because if query param is empty
    # like for the HOME PAGE
    # then it will NOT pass None BUT pass " " so we see the home page not ERROR
    posts = Post.objects.filter(
        Q(topic__title__icontains=query_param)
        # | Q(title__icontains=query_param)
        # | Q(content__icontains=query_param)
    )
    # IMP: posts are being filtered using OR condition, query_param can be
    # anything and it will search filter them
    # NOTE: icontains is case insensitive, and does partial matches TOO
    # so 'tel' can still work to find 'television'
    # NOTE: topic __ (double _) title means for "topic" var in Post
    # go to the parent of this "topic" var and get the "title"
    # i.e the foreign key
    topics = Topic.objects.all()
    # comments = Comment.objects.filter(post__title__icontains=)
    posts_count = posts.count()
    # comments_count = comments.count()
    post_comments = Comment.objects.filter(
        Q(post__topic__title__icontains=query_param)
    )
    # NOTE: post --> topic --> title

    context = {
        "posts": posts,
        "topics": topics,
        "post_comments": post_comments,
        "posts_count": posts_count,
        # "comments_count": comments_count,
    }
    return render(request, "main_app/home.html", context)


def about(request):
    return render(request, "main_app/about.html")


def post(request, post_id):
    post = Post.objects.get(id=post_id)

    post_comments = post.comment_set.all().order_by("-created_at")

    if request.method == "POST":
        comment = Comment.objects.create(
            owner=request.user,
            post=post,
            content=request.POST.get("body"),
        )
        return redirect("post", post_id=post.id)

    context = {"post": post, "post_comments": post_comments}
    # value we get from <int:post_id> is passed to
    # this function, and we can pass on this value to the template
    # using "context" which should be a dict
    return render(request, "main_app/post.html", context)
