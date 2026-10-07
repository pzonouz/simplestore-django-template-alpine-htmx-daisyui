from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from admin_panel.views import adminPanel
from core.views import home

urlpatterns = (
    [
        path("admin_panel/", adminPanel),
        path(
            "admin_panel/categories/",
            include("categories.urls", namespace="categories"),
        ),
        path("admin/", admin.site.urls),
        path("", home, name="home"),
        path("products/", include("products.urls", namespace="products")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + debug_toolbar_urls()
)
