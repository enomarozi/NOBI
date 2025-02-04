from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('index.urls')),
    path('account/',include('accounts.urls')),
    path('admin/',include('dashboard.urls')),
    path('admin/',include('mobil.urls')),
    path('admin/',include('layanan.urls')),
    path('admin/',include('faq.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)