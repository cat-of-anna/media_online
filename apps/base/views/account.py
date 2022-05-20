from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.auth import AuthSerializer
from .. import models
from utils import return_code
import jwt
import datetime
from django.conf import settings
from utils.ext.auth import JwtTokenAuthentication


class AuthView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        # 表单校验
        serializer = AuthSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"code": return_code.FAILED_ERROR, "detail": serializer.errors})
        # 数据库校验
        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")
        user_object = models.UserInfo.objects.filter(username=username, password=password).first()
        if not user_object:
            return Response({"code": return_code.VALIDATE_ERROR, "detail": "用户名或密码错误"})

        # jwt获取token
        headers = {
            'tpy': 'jwt',
            'alg': 'HS256'
        }
        payload = {
            'user_id': user_object.id,
            'username': user_object.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=10)   # 设置超时时间
        }
        # 生成jwt token
        token = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm='HS256', headers=headers)

        return Response({"code": return_code.SUCCESS, "data": {"token": token, "username": user_object.username}})



class TestView(APIView):
    def get(self, request, *args, **kwargs):
        print(request.user.username)
        return Response("ok")