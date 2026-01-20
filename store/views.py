from django.http import HttpResponse
from django.shortcuts import render

from store import forms
from store.models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    context_dict = {
        'products':products
    }
    return render(request, 'store.html', context_dict)

def add_product(request):
    
    if request.method == 'POST':
        product_form = forms.ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
    
    product_form = forms.ProductForm()
    context_dict = {
        'product_form':product_form
    }
    return render(request, 'add_product.html', context_dict)
