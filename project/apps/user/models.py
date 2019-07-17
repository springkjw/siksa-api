from django.db import models
from django.contrib import auth
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, Group, Permission,
    _user_get_all_permissions, _user_has_module_perms, _user_has_perm,
)

from .images import user_profile_image_path
from .enums import Gender, SocialProvider


class UserManager(BaseUserManager):
    # 식사 유저 매니저
    def _create_user(self, **kwargs):
        email = kwargs.get('email')
        password = kwargs.pop('password')

        if email is None:
            raise ValueError(
                "이메일은 필수입니다."
            )

        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password=None, **kwargs):
        if password is None:
            raise ValueError(
                "관리자는 비밀번호가 필수입니다."
            )

        kwargs.update({
            'password': password,
            'is_admin': True,
            'gender': Gender.ETC
        })

        return self._create_user(**kwargs)


class User(AbstractBaseUser):
    """
    식사 유저 모델
    """
    email = models.EmailField(
        '이메일',
        unique=True
    )
    password = models.CharField(
        '비밀번호',
        max_length=128,
        null=True,
        blank=True
    )

    name = models.CharField(
        '이름',
        max_length=202,
        null=True,
        blank=True
    )
    profile_image = models.ImageField(
        '프로필 이미지',
        upload_to=user_profile_image_path,
        null=True,
        blank=True
    )
    phone_number = models.CharField(
        '휴대전화',
         max_length=11,
         null=True,
         blank=True
    )
    is_phone_authenticate = models.BooleanField(
        '휴대전화 인증 여부',
        default=False
    )

    nickname = models.CharField(
        '닉네임',
        max_length=20,
        null=True,
        blank=True
    )
    gender = models.SmallIntegerField(
        '성별',
        choices=Gender.choices(),
        default=Gender.ETC
    )
    last_login = models.DateTimeField(
        '마지막 로그인',
        blank=True,
        null=True
    )
    date_joined = models.DateTimeField(
        '가입일',
        auto_now_add=True
    )

    is_active = models.BooleanField(
        '활성화 여부',
        default=True
    )
    is_admin = models.BooleanField(
        '관리자 여부',
        default=False
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name='그룹',
        blank=True,
        related_name="user_set",
        related_query_name="user"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='유저 권한',
        blank=True,
        related_name="user_set",
        related_query_name="user",
    )

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        db_table = 'users'
        verbose_name = '유저'
        verbose_name_plural = '유저들'

    def __str__(self):
        return "[{id}] {email}".format(id=self.id, email=self.email)

    def is_superuser(self):
        return self.is_active and self.is_admin

    def is_staff(self):
        return self.is_superuser()

    def get_group_permissions(self, obj=None):
        permissions = set()
        for backend in auth.get_backends():
            if hasattr(backend, 'get_group_permissions'):
                permissions.update(backend.get_group_permissions(self, obj))
        return permissions

    def get_all_permissionns(self, obj=None):
        return _user_get_all_permissions(self, obj)

    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_admin:
            return True

        return _user_has_perm(self, perm, obj)

    def has_perms(self, perm_list, obj=None):
        return all(self.has_perm(perm, obj) for perm in perm_list)

    def has_module_perms(self, app_label):
        if self.is_active and self.is_admin:
            return True

        return _user_has_module_perms(self, app_label)


class DropUser(models.Model):
    """
    탈퇴 유저 모델
    """
    user = models.ForeignKey(
        'User',
        verbose_name='유저',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'user_dropusers'
        verbose_name = '탈퇴 유저'
        verbose_name_plural = '탈퇴 유저들'

    def __str__(self):
        return str(self.user)


class SocialUser(models.Model):
    """
    소셜 로그인 모델
    """
    user = models.ForeignKey(
        User,
        verbose_name='유저',
        on_delete=models.CASCADE
    )
    provider = models.CharField(
        '공급자',
        max_length=15,
        choices=SocialProvider.choices()
    )
    uid = models.CharField(
        '플랫폼 고유 아이디',
        max_length=100
    )
    

    class Meta:
        db_table = 'user_socials'
        verbose_name = '소셜 로그인'
        verbose_name_plural = '소셜 로그인들'

    def __str__(self):
        return self.user
