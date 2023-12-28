from django.urls import include, path

from deepay.apps.landing.views import LandingView

app_name = "landing"

urlpatterns = [
    path("", LandingView.as_view(), name="landing"),
]
