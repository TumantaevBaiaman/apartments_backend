from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .yasg import urlpatterns as doc_url

api_urls = [
    path("managers/", include("apps.managers.urls")),
    path("", include("apps.apartments.urls")),
]

urlpatterns = [
    path("api/", include(api_urls)),
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]

urlpatterns += doc_url
