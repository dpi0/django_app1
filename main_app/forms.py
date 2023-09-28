from django.forms import ModelForm
from .models import Post, Comment


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
