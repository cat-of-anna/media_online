from django.urls import path, include
# 最后一次测试

urlpatterns = [
    path("api/base/", include('apps.base.urls')),
]
