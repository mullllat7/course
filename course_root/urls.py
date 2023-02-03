from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter

from course_root import settings

schema_view = get_schema_view(
    openapi.Info(
        title='Authentication API',
        default_version='v1',
        description='Test Description',
    ),
    public=True
)
router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('app.account.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
