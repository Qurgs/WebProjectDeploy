from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from Cinema.views import welcome, typing_game


schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', welcome, name='welcome_page'),
    path("admin/", admin.site.urls),
    path('api/v1/', include('Cinema.urls')),
    path('api/v1/', include('Review.urls')),
    path('api/v1/', include('User.urls')),
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0),
         name='schema-swagger-ui'
         ),
]
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
