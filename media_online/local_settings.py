DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'media_online',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '8.130.102.77',    # 远程主机
        'PORT': '3306',
    }
}

# rest_framework的配置
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ["utils.ext.auth.JwtTokenAuthentication"],
    "UNAUTHENTICATED_USER": lambda: None,
    "UNAUTHENTICATED_TOKEN": lambda: None
}