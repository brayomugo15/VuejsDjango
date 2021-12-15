from django.db import reset_queries
from django.http import JsonResponse, response
from .models import Product, Manufacturer

# Endpoints
def product_list(request):
    products = Product.objects.all()
    data = {"products": list(products.values())} # "pk", "name"
    response = JsonResponse(data)
    return response

def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {"product": {
            "name": product.name,
            "manufacturer": product.manufacturer.name,
            "description": product.description,
            "photo": product.photo.url,
            "price": product.price,
            "shippingcost": product.shippingcost,
            "quantity": product.quantity
        }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "product not found!"
            }},
            status=404)

    return response

# Competency test
def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        data = {"manufacturer": {
            "name": manufacturer.name,
            "location": manufacturer.location,
            "active": manufacturer.active,
        }}
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "manufacturer not found!"
            }},
            status=404)
    return response

def manufacturer_list(request):
    manufacturer = Manufacturer.objects.all()
    data = {"manufacturer": list(manufacturer.values())}
    response = JsonResponse(data)
    return response

# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView


# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_detail.html"

# class ProductListView(ListView):
#     model = Product
#     template_name = "products/product_list.html"

