from enum import Enum, IntEnum, unique


@unique
class Gender(IntEnum):
    """
    유저 성별 종류
    """
    MALE = 0        # 남자
    FEMALE = 1      # 여자
    ETC = 2         # 기타

    @classmethod
    def choices(cls):
        return (
            (cls.MALE.value, '남자'),
            (cls.FEMALE.value, '여자'),
            (cls.ETC.value, '기타'),
        )


@unique
class SocialProvider(Enum):
    """
    소셜 로그인 공급자 종류
    """
    FACEBOOK = 'facebook'
    KAKAO = 'kakao'
    NAVER = 'naver'

    @classmethod
    def choices(cls):
        return (
            (cls.FACEBOOK.value, '페이스북'),
            (cls.KAKAO.value, '카카오'),
            (cls.NAVER.value, '네이버'),
        )
