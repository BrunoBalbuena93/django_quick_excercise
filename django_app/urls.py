from django.conf import settings

from django.urls import include, path, re_path
from django.contrib import admin

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from oauth2_provider import views as oauth2_views

urlpatterns = []

if settings.DEBUG:
    urlpatterns += [
        re_path (r'^admin/', admin.site.urls),
    ]

urlpatterns += [
    path(
        'api-v0-jwt/token/',
        TokenObtainPairView.as_view(),
        name='jwt-token-obtain-pair'
    ),
    path(
        'api-v0-jwt/token/refresh/',
        TokenRefreshView.as_view(),
        name='jwt-token-refresh'
    )
]

urlpatterns += [
    path (
        'api-v0-dot/authorize/',
        oauth2_views.AuthorizationView.as_view (),
        name = "authorize"
    ),
    path (
        'api-v0-dot/token/',
        oauth2_views.TokenView.as_view (),
        name = "token"
    ),
    path (
        'api-v0-dot/revoke-token/',
        oauth2_views.RevokeTokenView.as_view (),
        name = "revoke-token"
    ),
    path (
        'api-v0-dot/introspect/',
        oauth2_views.IntrospectTokenView.as_view (),
        name = "instrospect"
    )
]

urlpatterns += [
    re_path (
        r'^api-v0/',
        include (
            (
                'users_pets_api.urls',
                'users_pets_api'
            ),
            namespace = 'users_pets_api'
        )
    )
]
