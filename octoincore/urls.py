from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.decorators.csrf import csrf_exempt
from strawberry.django.views import GraphQLView
from strawberry_django_jwt.decorators import jwt_cookie
from strawberry_django_jwt.views import StatusHandlingGraphQLView as GQLView

from octoincore.schema import schema

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^graphql/?$', jwt_cookie(GQLView.as_view(schema=schema))),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
