from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'index.html')



def login(request):
	return render(request, 'login.html')



def admin(request):
	return render(request, 'admin.html')



def teacher(request):
	return render(request, 'teacher.html')


def student(request):
	return render(request, 'student.html')