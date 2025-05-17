from django.views.generic import DetailView, ListView, TemplateView

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = "catalog/products_list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"
