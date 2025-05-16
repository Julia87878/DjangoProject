# from django.shortcuts import get_object_or_404, render
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


# def products_list(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, "catalog/products_list.html", context)
#
#
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, "catalog/product_detail.html", context)
#
#
# def contacts(request):
#     return render(request, "catalog/contacts.html")
