from django.urls import path

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("products_list/", views.products_list, name="products_list"),
    path("products/", views.products_list, name="products_list"),
    path("products/<int:pk>/", views.product_detail, name="product_detail"),
    path("contacts/", views.contacts, name="contacts"),
]
