from django.urls import path

from catalog.apps import CatalogConfig

from .views import (
    CategoryDetailView,
    CategoryListView,
    ContactsTemplateView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
    UnpublishProductView,
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
    path(
        "products/unpublish/<int:pk>/",
        UnpublishProductView.as_view(),
        name="product_unpublish",
    ),
    path("categories/", CategoryListView.as_view(), name="categories_list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category_detail"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
]
