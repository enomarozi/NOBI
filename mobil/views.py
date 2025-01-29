from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .forms import CustomFormMobil
from .models import KelolaMobil

def mobil(request):
	form = CustomFormMobil()
	if request.method == "POST":
		form = CustomFormMobil(data=request.POST)
		if request.POST.get('action') == "Hapus":
			id_mobil = get_object_or_404(KelolaMobil, id=request.POST.get('id'))
			id_mobil.delete()
		else:
			if form.is_valid():
				if request.POST.get('action') == "Tambah":
					merek = form.cleaned_data.get("merek")
					kapasitas = form.cleaned_data.get("kapasitas")
					durasi = form.cleaned_data.get("durasi")
					harga = form.cleaned_data.get("harga")
					addCar = KelolaMobil(merek=merek, kapasitas=kapasitas, durasi=durasi, harga=harga)
					addCar.save()
				elif request.POST.get('action') == "Edit":
					id_mobil = get_object_or_404(KelolaMobil, id=request.POST.get('id'))
					form = CustomFormMobil(data=request.POST, instance=id_mobil)
					form.save()
			

	return render(request, 'admin/mobil.html', {"form":form})

def getMobil(request):
	mobil = KelolaMobil.objects.all().values('id','merek','kapasitas','durasi','harga')
	return JsonResponse(list(mobil), safe=False)