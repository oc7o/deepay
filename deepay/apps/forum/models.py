from django.db import models
from deepay.apps.users.models import ExtendUser as User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Vote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(-1, "Downvote"), (1, "Upvote")])

    def __str__(self):
        return f"{self.voter.username} voted {self.value} on {self.post.title}"
