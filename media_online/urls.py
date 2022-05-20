from django.urls import path, include
# from django.conf import settings
# 测试
# 测试3好

urlpatterns = [
    path("api/base/", include('apps.base.urls')),
]
