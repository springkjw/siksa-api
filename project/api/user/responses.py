from rest_framework import serializers


class UserLoginSuccessResponse(serializers.Serializer):
    token = serializers.CharField(
        label='토큰'
    )


class UserLoginFailResponse(serializers.Serializer):
    message = serializers.CharField(
        label='메세지',
        default='이메일과 비밀번호를 다시 한번 확인해주세요.'
    )
    code = serializers.CharField(
        label='에러 코드',
        default='WRONG CREDENTIALS'
    )

    def json(self):
        return {
            'message': '이메일과 비밀번호를 다시 한번 확인해주세요.',
            'code': 'WRONG CREDENTIALS'
        }


class UserDuplicateResponse(serializers.Serializer):
    is_duplicate = serializers.BooleanField(
        label='이메일 중복 여부'
    )