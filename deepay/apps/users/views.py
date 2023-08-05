from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.views.generic import DetailView, TemplateView


class LoginView(DjangoLoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True


class LogoutView(DjangoLogoutView):
    # template_name = "users/logout.html"
    pass


class ProfileView(TemplateView):
    # model = get_user_model()
    template_name = "users/profile.html"
    # context_object_name = "user"
