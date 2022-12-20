from . import views
from django.urls import path
# Create your views here.
urlpatterns = [
	path('', views.store, name='store'),
	path('cart/', views.cart, name='cart'),
	path('checkout/', views.checkout, name='checkout'),
]