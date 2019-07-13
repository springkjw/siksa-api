DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'drf_yasg',
]

PROJECT_APPS = [
    'apps.admin.config.AdminConfig',
    'apps.user',
    'apps.mentor',
    'apps.ticket',
    'apps.order',
]

INSTALLED_APPS = THIRD_PARTY_APPS + PROJECT_APPS + DJANGO_APPS
