from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql", GraphQLView.as_view(graphiql=True)),
    path("", include("octoincore.dashboard.urls")),
    # path("console/", include("octoincore.console.urls")),
    # path("fileserver/", include("octoincore.fileserver.urls")),
]
