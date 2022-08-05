from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from store.models import Product
# Create your views here.

def say_hello(request):
    # return HttpResponse('Hello World , I am Vineet  and I am running Django server')
    # try:
    #     product= Product.objects.get(pk=1)
    # except:
    #     pass

    # product= Product.objects.filter(pk=1).first()
    
    exists= Product.objects.filter(pk=1).exists()

    queryset = Product.objects.filter()

    return render(request, 'helloworld.html' )
