from django.shortcuts import render
from .forms import CustomFormMobil

def mobil(request):
	form = CustomFormMobil()
	if request.method == "POST":
		form = CustomFormMobil(data=request.POST)
		if form.is_valid():
			merek = form.cleaned_data.get("merek")
			kapasitas = form.cleaned_data.get("kapasitas")
			durasi = form.cleaned_data.get("durasi")
			harga = form.cleaned_data.get("harga")
			car = 123
	return render(request, 'admin/mobil.html', {"form":form})

def artikel(request):
	return render(request, 'admin/artikel.html')