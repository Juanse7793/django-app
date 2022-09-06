from django.shortcuts import render
from django.http import HttpResponse
import pkg_resources
from store.models import Product




def say_hello(request):
    query_set = Product.objects.filter(title__icontains='coffee')
    
    
    return render(request, 'hello.html', {'name': 'Juan', 'products': query_set})
