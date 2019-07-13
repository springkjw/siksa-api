from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('', views.UserViewSet)

urlpatterns = [
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('signup/', views.SignUpAPIView.as_view(), name='signup'),
] + router.urls
