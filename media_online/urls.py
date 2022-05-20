from django.urls import path, include
# from django.conf import settings
# 测试
# 测试3好
# 测试4好
# 最后一次测试
# 最后一次测试，啊啊啊啊


urlpatterns = [
    path("api/base/", include('apps.base.urls')),
]
