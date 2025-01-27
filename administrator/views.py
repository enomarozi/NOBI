from django.shortcuts import render
from django.http import JsonResponse
from .forms import CustomFormMobil
from .models import KelolaMobil

def mobil(request):
	form = CustomFormMobil()
	if request.method == "POST":
		form = CustomFormMobil(data=request.POST)
		if form.is_valid():
			merek = form.cleaned_data.get("merek")
			kapasitas = form.cleaned_data.get("kapasitas")
			durasi = form.cleaned_data.get("durasi")
			harga = form.cleaned_data.get("harga")
			addCar = KelolaMobil(merek=merek, kapasitas=kapasitas, durasi=durasi, harga=harga)
			addCar.save()
	return render(request, 'admin/mobil.html', {"form":form})

def getMobil(request):
	mobil = KelolaMobil.objects.all().values('merek','kapasitas','durasi','harga')
	return JsonResponse(list(mobil), safe=False)

def artikel(request):
	return render(request, 'admin/artikel.html')