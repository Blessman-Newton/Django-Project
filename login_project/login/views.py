from django.shortcuts import render,redirect
from .form import Pro
from .models import Form
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'index.html')


def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		password_confirm = request.POST['password_confirm']
		email = request.POST['email']
		if password == password_confirm:
			if User.objects.filter(email=email).exists():
				messages.info(request, 'Email Already exist')
				return redirect('register')
			elif User.objects.filter(username=username):
				messages.info(request, 'Username Already exist')
				return redirect('register')
			else:
				user = User.objects.create_user(username=username, password=password, email=email)
				user.save()
				return redirect('login')
		else:
			messages.info(request ,'Wrong password')
			return redirect('register')
	return render(request, 'register.html')


def login(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		try:
		 	User.objects.get(username=username)
		except:
			messages.info(request, 'User does not exist')

		user = auth.authenticate(request, username=username, password=password)

		if user is not None:
			auth.login(request,user)
			return redirect('index')
		else:
			messages.info(request, 'User does not exist')
			return redirect('login')
	return render(request, 'login.html')


def update(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		password_confirm = request.POST['password_confirm']
		email = request.POST['email']
		if password == password_confirm:
			if User.objects.filter(email=email).exists():
				messages.info(request, 'Email Already exist')
				return redirect('register')
			elif User.objects.filter(username=username):
				messages.info(request, 'Username Already exist')
				return redirect('register')
			else:
				user = User.objects.create_user(username=username, password=password, email=email)
				user.save()
				return redirect('login')
		else:
			messages.info(request ,'Wrong password')
			return redirect('register')
	return render(request, 'update.html')


	

