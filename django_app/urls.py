from django.conf import settings

from django.urls import include, path, re_path
from django.contrib import admin

urlpatterns = []

if settings.DEBUG:
    urlpatterns += [
        re_path (r'^admin/', admin.site.urls),
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
