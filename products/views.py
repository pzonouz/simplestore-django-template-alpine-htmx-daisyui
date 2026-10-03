from django.shortcuts import render

from products.admin import Product


def featured_products_partials(request):
    products = Product.objects.all()
    return render(
        request, "partials/products/featured_list.django", {"products": products}
    )
