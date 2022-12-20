from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=20)
	address = models.CharField(max_length=20)

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=20)
	price = models.FloatField(default=0,null=True, blank=True)
	change_price = models.FloatField(default=0,null=True, blank=True)
	digital = models.BooleanField(default=True)
	image = models.ImageField(null=True, blank=True)


	def __str__(self):
		return self.name

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True , blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complated = models.BooleanField(default=True, null=True , blank=True)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True , blank=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True , blank=True)
	quanity = models.IntegerField(default=0,null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)



class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True , blank=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True , blank=True)
	address = models.CharField(max_length=20, null=True)
	city = models.CharField(max_length=20,null=True)
	state = models.CharField(max_length=20,null=True)
	zipcode = models.IntegerField(default=0,null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.address

