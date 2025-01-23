from django.urls import path
from . import views

urlpatterns = [
	path('mobil/', views.mobil, name='mobil'),
	path('artikel/', views.artikel, name='artikel'),
]