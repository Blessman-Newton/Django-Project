from django.urls import path
from . import views


urlpatterns = [
	path('',views.index, name='index'),
	path('login/',views.login, name='login'),
	path('admin/',views.admin, name='admin'),
	path('teacher/',views.teacher, name='teacher'),
	path('student/',views.student, name='student'),
	

]