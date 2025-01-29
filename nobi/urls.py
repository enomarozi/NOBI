from django.urls import path, include

urlpatterns = [
    path('',include('accounts.urls')),
    path('admin/',include('mobil.urls')),
    path('admin/',include('artikel.urls')),
]