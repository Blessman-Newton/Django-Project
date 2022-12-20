from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout
from django.contrib import messages
# Create your views here.

def index(request):
	return render(request, 'index.html')


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		try:
			User.objects.get(username=username)
		except:
			messages.info(request,  'User already exist')

		user = auth.authenticate(request, username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'User already exist')
			return redirect('login')
	return render(request, 'login.html')


def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']
		if password == confirm_password:
			if User.objects.filter(email=email).exists():
				messages.info(request,'email already exist')
				return redirect('register')
			elif User.objects.filter(username=username).exists():
				messages.info(request,'User already exist')
				return redirect('register')
			else:
				user = User.objects.create_user(username=username, email=email, password=password)
				user.save()
				return redirect('login')
		else:
			messages.info(request,"Passwors doesn't match")
			return redirect('register')
	return render(request, 'register.html')


def home(request):
	return render(request, 'home.html')


def logout(request):
	auth.logout(request)
	return redirect('index')





