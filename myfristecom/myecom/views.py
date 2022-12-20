from django.shortcuts import render
from .models import *

# Create your views here.
def store(request):
	products = Product.objects.all()
	context = {
		'products':products
		
	}
	return render(request, 'store.html', context)


def cart(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order,created = Order.objects.get_or_create(customer=customer, complated=False)
		items = Order.objects.all()
	else:
		items = []
		 
	context = {
		'items':items
	}
	return render(request, 'cart.html',context)


def checkout(request):
	return render(request, 'checkout.html')
