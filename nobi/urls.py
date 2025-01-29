from django.urls import path, include

urlpatterns = [
    path('',include('dashboard.urls')),
    path('account/',include('accounts.urls')),
    path('admin/',include('dashboard.urls')),
    path('admin/',include('mobil.urls')),
    path('admin/',include('layanan.urls')),
]