from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.views.generic import DetailView, TemplateView, UpdateView, ListView
from django.urls import reverse

from deepay.apps.inventory.models import Product


class LoginView(DjangoLoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True


class LogoutView(DjangoLogoutView):
    # template_name = "users/logout.html"
    pass


# class ProfileView(DetailView):
#     model = get_user_model()
#     template_name = "users/profile.html"

#     def get_object(self, queryset=None):
#         return get_user_model().objects.get(username=self.kwargs["username"])

#     # context_object_name = "user"


class ProfileView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "users/profile.html"

    paginate_by = 8

    # def get_object(self, queryset=None):
    #     return get_user_model().objects.get(username=self.kwargs["username"])

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["object"] = get_user_model().objects.get(
            username=self.kwargs["username"]
        )
        return context

    def get_queryset(self):
        return Product.objects.filter(owner__username=self.kwargs["username"])

    # context_object_name = "user"


class ProfileSettingsView(UpdateView):
    template_name = "users/settings.html"
    model = get_user_model()
    fields = ["email", "profile_image"]

    def get_success_url(self) -> str:
        return reverse("users:profile")

    def get_object(self, queryset=None):
        return self.request.user
