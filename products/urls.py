from django.urls import path

from products.views import featured_products_partials

app_name = "products"

urlpatterns = [path("featured_list/", featured_products_partials, name="featured_list")]
