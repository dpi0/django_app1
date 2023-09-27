from django.contrib import admin

# Register your models here.
from .models import Post, Topic

admin.site.register(Post)
admin.site.register(Topic)
