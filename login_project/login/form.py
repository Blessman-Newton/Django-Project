from django.db import models
from django.contrib.auth.models import User
from django import forms

class Pro(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','email','password']
