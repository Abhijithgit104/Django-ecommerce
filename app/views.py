from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import product

def home(request):
    return render(request, 'app/home.html')

def products(request):
    products = product.objects.all()
    return render(request, 'app/products.html', {'products': products})

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')
