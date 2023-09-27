from django.shortcuts import render

# from django.http import HttpResponse

# Create your views here.


temp_db = [
    {"post_id": 1, "title": "post 1", "content": "content 1"},
    {"post_id": 2, "title": "post 2", "content": "content 2"},
    {"post_id": 3, "title": "post 3", "content": "content 3"},
    {"post_id": 4, "title": "post 4", "content": "content 4"},
]


def home(request):
    passing_to_template = {"posts": temp_db}
    return render(request, "main_app/home.html", passing_to_template)


def about(request):
    return render(request, "main_app/about.html")


def post(request, post_id):
    post = None
    for temp_post in temp_db:
        if temp_post["post_id"] == post_id:
            post = temp_post
    context = {"post": post}
    # value we get from <int:post_id> is passed to
    # this function, and we can pass on this value to the template
    # using "context" which should be a dict
    return render(request, "main_app/post.html", context)
