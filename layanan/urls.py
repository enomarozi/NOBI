from django.urls import path
from . import views

urlpatterns = [
	path('layanan/', views.layanan, name='layanan'),
	path('getLayanan/', views.getLayanan, name='getLayanan'),
]