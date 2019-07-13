from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated, AllowAny

schema_view = get_schema_view(
   openapi.Info(
      title="식사 API",
      default_version='v1',
      description="식사 Django API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="springkjw@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=False,
   permission_classes=(AllowAny,),
   patterns=[
       path('api/', include(('api.urls', 'api'), namespace='api')),
   ]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('api.urls', 'api'), namespace='api')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
