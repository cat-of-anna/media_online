from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import jwt
from django.conf import settings
from utils import return_code


class CurrentUser(object):
    def __init__(self, user_id, username, exp):
        self.user_id = user_id
        self.username = username
        self.exp = exp


class StatusAuthenticationFailed(AuthenticationFailed):
    status_code = 200


class JwtTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        """
        读取用户提交的jwt_token，进行校验，返回一个元组
        :param request:
        :return:(request.user, request.auth)
        """
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            raise StatusAuthenticationFailed({"code": return_code.AUTH_FAILED, "error": "认证失败"})
        # jwt校验token
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, ["HS256"])
            print(payload)
        except Exception as e:
            raise StatusAuthenticationFailed({"code": return_code.AUTH_FAILED, "error": "认证失败"})

        return CurrentUser(**payload), token

    def authenticate_header(self, request):
        return 'Bearer realm="API"'


