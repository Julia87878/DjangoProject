from django.urls import path

from catalog.apps import CatalogConfig

from .views import (
    ContactsTemplateView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("products/", ProductListView.as_view(), name="products_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("products/new/", ProductCreateView.as_view(), name="product_create"),
    path(
        "products/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "products/delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
]
