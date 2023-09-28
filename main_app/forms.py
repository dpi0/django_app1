from django.forms import ModelForm
from .models import Post, Comment, User


# NOTE: this uses the fields of "Post" model & uses django's ModelForm to auto
# create the form
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ["owner", "created_at", "updated_at"]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        # fields = "__all__"


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]
