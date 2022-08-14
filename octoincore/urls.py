from django.contrib import admin
from django.urls import path, include, re_path

from strawberry.django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from strawberry_django_jwt.decorators import jwt_cookie
from strawberry_django_jwt.views import StatusHandlingGraphQLView as GQLView

from octoincore.schema import schema

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^graphql/?$', jwt_cookie(GQLView.as_view(schema=schema))),
    # path("", include("octoincore.dashboard.urls")),
    # path("console/", include("octoincore.console.urls")),
    # path("fileserver/", include("octoincore.fileserver.urls")),
]