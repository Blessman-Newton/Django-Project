from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
	product = Product.objects.all()
	return render(request, 'index.html', {'product':product})


def search(request):
	if request.method == 'POST':
		q = request.POST['q']
		if q:
			product = Product.objects.filter(name__icontains=q)
			return render(request, 'search.html', {'product':product})
		else:
			print('No information to show')
			return render(request, 'search.html', {})

	