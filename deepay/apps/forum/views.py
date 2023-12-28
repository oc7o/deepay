from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from deepay.apps.forum.models import Thread


class ThreadListView(ListView):
    model = Thread


class ThreadPostsView(DetailView):
    model = Thread


class ThreadCreateView(CreateView):
    model = Thread
    fields = ["slug", "image"]

    def get_success_url(self) -> str:
        return reverse("forum:thread-detail", kwargs={"slug": self.object.slug})
