# users/auth_extensions.py fayli. Ushbu fayl Custom JWT Authentication Scheme yaratish uchun.

from drf_spectacular.contrib.rest_framework_simplejwt import SimpleJWTScheme

from .authentications import CustomJWTAuthentication

class CustomJWTAuthenticationScheme(SimpleJWTScheme):
    name = "CustomJWTAuth"
    target_class = CustomJWTAuthentication