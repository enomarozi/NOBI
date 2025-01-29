from django.urls import path
from . import views

urlpatterns = [
	path('artikel/', views.artikel, name='artikel'),
	# path('getArtikel/', views.getArtikel, name='getArtikel'),
]