from django.urls import path, include


urlpatterns = [
    path("api/base/", include('apps.base.urls')),
]
