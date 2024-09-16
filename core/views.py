from django.shortcuts import render
from principia.models import Product

def frontpage(request):
    products = Product.objects.all()[0:10]
    return render(request, 'core/frontpage.html', {'products': products})

def sobre(request):
    return render(request, 'core/sobre.html')