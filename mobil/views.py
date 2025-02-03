from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from .forms import CustomFormMobil
from .models import KelolaMobil
import os
def mobil(request):
	form = CustomFormMobil()
	if request.method == "POST":
		form = CustomFormMobil(request.POST, request.FILES)
		if request.POST.get('action') == "Hapus":
			id_mobil = get_object_or_404(KelolaMobil, id=request.POST.get('id'))
			os.system("rm uploads/"+id_mobil.filename)
			id_mobil.delete()

		else:
			if request.POST.get('action') == "Tambah":
				if form.is_valid():
					filename = form.cleaned_data.get("filename")
					fs = FileSystemStorage()
					name = fs.save(filename.name, filename)
					merek = form.cleaned_data.get("merek")
					kapasitas = form.cleaned_data.get("kapasitas")
					durasi = form.cleaned_data.get("durasi")
					harga = form.cleaned_data.get("harga")
					addCar = KelolaMobil(filename=name, merek=merek, kapasitas=kapasitas, durasi=durasi, harga=harga)
					addCar.save()
			elif request.POST.get('action') == "Edit":
				id_mobil = get_object_or_404(KelolaMobil, id=request.POST.get('id'))
				form = CustomFormMobil(data=request.POST, instance=id_mobil, files=request.FILES)
				if form.is_valid():
					filename = form.cleaned_data.get("filename")
					fs = FileSystemStorage()
					name = fs.save(filename.name, filename)
					form.save()	

	return render(request, 'admin/mobil.html', {"form":form})

def getMobil(request):
	mobil = KelolaMobil.objects.all().values('id','filename','merek','kapasitas','durasi','harga')
	return JsonResponse(list(mobil), safe=False)