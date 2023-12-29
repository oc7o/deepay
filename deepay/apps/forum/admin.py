from django.contrib import admin
from .models import Thread, Post, Comment, Vote

admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Vote)
