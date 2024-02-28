from django.urls import path

from deepay.apps.users.views import (
    LoginView,
    LogoutView,
    ProfileView,
    ProfileSettingsView,
)

app_name = "users"

urlpatterns = [
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("u/<slug:username>/", ProfileView.as_view(), name="profile"),
    path("accounts/settings/", ProfileSettingsView.as_view(), name="settings"),
]
