from django.shortcuts import render
from django.contrib.auth.models import User
from ..models import Topic
from django.db.models import Q


def user_profile(request, username):
    query_param = (
        request.GET.get("q") if request.GET.get("q") is not None else ""
    )
    # user = User.objects.get(id=user_id)
    user = User.objects.get(username=username)
    posts = user.post_set.all()
    # filter_post = posts.filter(Q(topic__title__icontains=query_param))
    post_comments = user.comment_set.all()
    topics = Topic.objects.all()

    context = {
        "user": user,
        "posts": posts,
        # "filter_posts": filter_post,
        "post_comments": post_comments,
        "topics": topics,
    }
    return render(request, "main_app/profile.html", context)
