# users/enums.py fayli Token type ni ajratish uchun kerak bo’ladi

from enum import Enum

class TokenType(str, Enum):
    ACCESS = "access"
    REFRESH = "refresh"

