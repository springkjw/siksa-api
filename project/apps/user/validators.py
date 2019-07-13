from django.core.exceptions import ValidationError


def validate_phone_number(value):
    """
    전화번호 인증
    01012341234 형식만 지원
    """
    pass