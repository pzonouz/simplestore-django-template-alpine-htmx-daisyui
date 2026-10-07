from django.urls import path

from . import views

app_name = "categories"

urlpatterns = [
    path("", views.category_list, name="list"),
    path("create/", views.category_create, name="create"),
    path("show/<str:id>", views.category_view, name="show"),
    path("edit/<str:id>", views.category_edit, name="edit"),
]
