from django.shortcuts import render
from .models import Product # .models is a relitave import
from .forms import ProductForm, RawProductForm # Create a form using django models


# Create your views here.

## Using Django to autobuild form
# def product_create_view(request):
#     form = ProductForm(request.POST or None) #
#     if form.is_valid():
#         form.save()
#         form = ProductForm() # Rerender the view after it is saved

#     context = {
#         "site_title": "Create Product",
#         "form": form,
#     }
#     return render(request, "products/product_create.html", context)

## Using Django to build more complex form
def product_create_view(request):
    form = RawProductForm(request.POST or None) # Sees if it is a POST request else initilize as empty 
    if form.is_valid():
        Product.objects.create(**form.cleaned_data) # Placing the ** before it tells the model to treat from.cleaned_data as a dictionary of keyword arguments. Title = a, Price = 10 ...
        form = RawProductForm()
    context = {
        "site_title": "Create Product",
        "form": form
    }
    return render(request, "products/product_create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        "site_title": "Products",
        "object": obj,
    }
    return render(request, "products/product_detail.html", context)