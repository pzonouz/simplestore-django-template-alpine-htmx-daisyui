from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from categories.forms import CategoryForm
from categories.models import Category


def category_list(request):
    categories = Category.objects.select_related("parent").all()
    form = CategoryForm()
    context = {"categories": categories, "form": form}
    return render(request, "pages/index.html", context)


def category_view(request, id):
    category = get_object_or_404(Category, pk=id)
    response = render(
        request,
        "cotton/category/row.html",
        {"category": category},
    )
    return response


def category_create(request):
    if request.method != "POST":
        return HttpResponse(status=405)

    form = CategoryForm(request.POST)
    if form.is_valid():
        category = form.save()
        # Return only the new table row
        response = render(
            request,
            "cotton/category/row.html",
            {"category": category},
        )
        return response
    # If form has errors, return the form with status 422 Unprocessable Entity
    # and retarget the swap back to the form container
    response = render(
        request,
        "cotton/category/create.html",
        {"form": form},
    )
    # Tell HTMX to swap the form instead of the table row
    response["HX-Retarget"] = "#category-create-form"
    response["HX-Reswap"] = "outerHTML"
    return response


def category_edit(request, id):
    category = Category.objects.get(pk=id)
    if request.method != "POST":
        form = CategoryForm(instance=category)
        context = {"category": category, "form": form}
        return render(request, "cotton/category/row_form.html", context)

    form = CategoryForm(request.POST, instance=category)
    if form.is_valid():
        category = form.save()
        # Return only the new table row
        response = render(
            request,
            "cotton/category/row.html",
            {"category": category},
        )
        return response
    # If form has errors, return the form with status 422 Unprocessable Entity
    # and retarget the swap back to the form container
    response = render(
        request,
        "cotton/category/row_form.html",
        {"form": form, "category": category},
    )
    # Tell HTMX to swap the form instead of the table row
    # response["HX-Retarget"] = "#category-create-form"
    # response["HX-Reswap"] = "outerHTML"
    return response
