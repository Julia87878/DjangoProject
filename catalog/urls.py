from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactsTemplateView, ProductDetailView, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path("products/", ProductListView.as_view(), name="products_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
]

# urlpatterns = [
#     path("products/",views.products_list, name="products_list"),
#     path("products/<int:pk>/", views.product_detail, name="product_detail"),
#     path("contacts/", views.contacts, name="contacts"),
#  ]
