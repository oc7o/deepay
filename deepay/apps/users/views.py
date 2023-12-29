from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.views.generic import DetailView, TemplateView, UpdateView
from django.urls import reverse


class LoginView(DjangoLoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True


class LogoutView(DjangoLogoutView):
    # template_name = "users/logout.html"
    pass


class ProfileView(DetailView):
    model = get_user_model()
    template_name = "users/profile.html"

    def get_object(self, queryset=None):
        return get_user_model().objects.get(username=self.kwargs["username"])

    # context_object_name = "user"


class ProfileSettingsView(UpdateView):
    template_name = "users/settings.html"
    model = get_user_model()
    fields = ["email", "profile_image"]

    def get_success_url(self) -> str:
        return reverse("users:profile")

    def get_object(self, queryset=None):
        return self.request.user
