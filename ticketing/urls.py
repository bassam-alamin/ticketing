from decouple import config
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from django.views.generic.base import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

public_apis = [
    # urls for the auth app
    url(r'^api/v1/auth/', include("apps.auth_app.urls")),
    url(r'^api/v1/booking/', include("apps.booking.urls")),

]

schema_view = get_schema_view(
    openapi.Info(
        title=config("API_TITLE"),
        default_version=config("VERSION"),
        description="These are the main APIs for Ticketing App",
        terms_of_service=config("TnCS_URL"),
        x_logo={
            "url": config("LOGO_URL"),
            "backgroundColor": "#FFFFFF"
        }
    ),
    public=True,
    patterns=public_apis,
    permission_classes=(permissions.AllowAny,),
)
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path('developer/docs', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('developer/doc', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),
    path('favicon.ico', favicon_view),

    # enable the admin interface
    url(r'^admin/', admin.site.urls),
]

urlpatterns += public_apis
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = config('ADMIN_SITE_HEADER')
admin.site.site_title = config('ADMIN_SITE_TITLE')
admin.site.index_title = config('ADMIN_SITE_INDEX_TITLE')