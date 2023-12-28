from django.db import models

from deepay.apps.users.models import ExtendUser as User
from deepay.models import DefaultModel


class Thread(DefaultModel):
    slug = models.SlugField(unique=True)
    image = models.ImageField(
        upload_to="uploads/thread_icons/",
        blank=True,
        null=True,
        default="/static/defaults/placeholder.png",
    )


class Post(DefaultModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title


class Comment(DefaultModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Vote(DefaultModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(-1, "Downvote"), (1, "Upvote")])

    def __str__(self):
        return f"{self.voter.username} voted {self.value} on {self.post.title}"
