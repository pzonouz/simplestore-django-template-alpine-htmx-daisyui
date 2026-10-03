from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from core.views import home

urlpatterns = [
    path("dev-admin/", admin.site.urls),
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("products/", include("products.urls", namespace="products")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
