from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from deepay.apps.forum.models import Thread, Post
from deepay.mixins import SuperUserRequiredMixin


class ThreadListView(ListView):
    model = Thread


class ThreadDeleteView(SuperUserRequiredMixin, DeleteView):
    model = Thread
    success_url = reverse_lazy("forum:thread-list")


class ThreadPostsView(DetailView):
    model = Thread


class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    fields = ["slug", "image"]

    def get_success_url(self) -> str:
        return reverse("forum:thread-detail", kwargs={"slug": self.object.slug})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def get_success_url(self) -> str:
        return reverse("forum:post-detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        print(type(self.request.user))
        form.instance.author = self.request.user
        form.instance.thread = Thread.objects.get(slug=self.kwargs["slug"])
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        return Post.objects.get(web_id=self.kwargs["web_id"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comment_set.all()
        return context

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(web_id=self.kwargs["web_id"])

        if request.user.is_authenticated:
            if request.POST.get("comment") or request.POST.get("comment") == "comment":
                post.comment_set.create(
                    author=request.user, content=request.POST["content"]
                )
            return redirect(
                reverse("forum:post-detail", kwargs={"web_id": self.kwargs["web_id"]})
            )
        else:
            return redirect(reverse("users:login"))

    # # Maybe Later
    # def post(self, request, *args, **kwargs):
    #     post = Post.objects.get(pk=self.kwargs["pk"])
    #     if request.POST.get("upvote"):
    #         post.vote_set.create(voter=request.user, value=1)
    #     elif request.POST.get("downvote"):
    #         post.vote_set.create(voter=request.user, value=-1)
    #     return redirect(
    #         reverse("forum:post-detail", kwargs={"pk": self.kwargs["pk"]})
    #     )
