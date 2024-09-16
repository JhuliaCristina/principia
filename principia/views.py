from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def search(request):
    query=request.GET.get('query','')
    products = Product.objects.filter(title__icontains=query)
    return render(request,'principia/search.html',{'query':query, 'products':products})

def minha_loja(request):
    return render(request,'userprofile/minhaloja.html')

def category_details(request, slug):
    category = get_object_or_404(Category,slug=slug)
    poducts = category.products.all
    return render(request, 'principia/category_details.html',{ 'category': category, 'poducts': poducts})

def product_details(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request,'principia/product_details.html', {'product':product})

