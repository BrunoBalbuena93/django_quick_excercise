from django.conf import settings

from django.urls import include, path, re_path
from django.contrib import admin

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

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
