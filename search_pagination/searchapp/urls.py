from django.urls import path
from . import views
#from django.confi-static import static 
#from django.confi import settings


urlpatterns = [
	path('', views.index, name='index'),
	path('search', views.search, name='search'),
	
]

#urlpatterns += static(settings.MEDIA_URL,document-root == settings.MEDIA_ROOT)