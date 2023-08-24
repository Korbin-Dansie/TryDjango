from django.shortcuts import render
from .models import Product # .models is a relitave import

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        "site_title": "Products",
        "object": obj,
    }
    return render(request, "products/product_detail.html", context)