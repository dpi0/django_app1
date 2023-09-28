from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Comment
from ..forms import CommentForm
from django.http import HttpResponse


@login_required(login_url="login")
def update_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    form = CommentForm(instance=comment)

    if request.user != comment.owner:
        return HttpResponse("You are not the owner of this comment")

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "main_app/comment_form.html", context)


@login_required(login_url="login")
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)

    if request.user != comment.owner:
        return HttpResponse("You are not the owner of this post")

    if request.method == "POST":
        comment.delete()  # deletes the post
        return redirect("home")

    context = {"object_to_be_deleted": comment}
    return render(request, "main_app/delete.html", context)
