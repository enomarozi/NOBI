from django.urls import path
from . import views

urlpatterns = [
	path('faq/', views.FAQ, name='FAQ'),
	path('getFAQ/', views.getFAQ, name='getFAQ'),
]