from django.contrib import admin
from django.urls import path, include

from strawberry.django.views import GraphQLView
from octoincore.graphql.schema import schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql", GraphQLView.as_view(schema=schema)),
    path("", include("octoincore.dashboard.urls")),
    # path("console/", include("octoincore.console.urls")),
    # path("fileserver/", include("octoincore.fileserver.urls")),
]