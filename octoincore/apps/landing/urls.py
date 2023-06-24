from django.urls import path

from octoincore.apps.landing.views import LandingView

app_name = "landing"

urlpatterns = [
    path("", LandingView.as_view(), name="landing"),
]
