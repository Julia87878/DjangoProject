from django.shortcuts import render

from .models import Product


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "catalog/products_list.html", context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "catalog/product_detail.html", context)


def contacts(request):
    return render(request, "catalog/contacts.html")
