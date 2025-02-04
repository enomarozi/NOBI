from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('faq', views.home_faq, name='home_faq'),
]