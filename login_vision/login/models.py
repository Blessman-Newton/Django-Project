from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Form(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=200,null=True, blank=True)
	desription = models.TextField(null=True, blank=True)
	completed = models.BooleanField(default=True)
	created_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title


	class Meta: 
		ordering = ['completed']



	
		
