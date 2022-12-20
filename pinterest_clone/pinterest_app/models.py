from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Teacher(models.Model):
	name = models.CharField(max_lenght=50, null=False, blank=False)
	staff_id = models.CharField(max_lenght=20, null=False, blank=False)
	courses = models.CharField(max_lenght=20)

	def __str__(self):
		return self.name


class Subject(models.Model):
	javascript = models.IntegerField()
	php = models.IntegerField()
	java = models.IntegerField()
	python = models.IntegerField()



class Student(models.Model):
	username = ForeginKey(User, on_delete=models.CASCADE, null=False, blank=False)
	teacher = ForeginKey(Teacher, on_delete=models.CASCADE, null=True, blank=True
		)
	student_id = models.CharField(max_lenght=15)
	firstname = models.CharField(max_lenght=15)
	middle = models.CharField(max_lenght=15, null=True, blank=True)
	lastname = models.CharField(max_lenght=15)
	dob = models.DateField()
	home_town = models.CharField(max_lenght=20)
	parents_name= models.CharField(max_lenght=50, lable='One name')
	Day = BooleanField(default=True)
	courses = models.CharField(max_lenght=15)


	def __str__(self):
		return self.username



class Admin(models.Model):
	admin_id = CharField(max_lenght=20, null=False, blank=False)
	username = ForeginKey(User, on_delete=models.CASCADE, null=False, blank=False)


	def __str__(self):
		return self.username


class Result(models.Model):
	username = ForeginKey(Student, on_delete=models.CASCADE, null=False , blank=False)
	subject = ForeginKey(Subject, on_delete=models.CASCADE, null=False, blank=False)

	def __str__(self):
		return self.subject