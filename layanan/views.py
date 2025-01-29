from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .forms import CustomFormLayanan
from .models import KelolaLayanan

def layanan(request):
	form = CustomFormLayanan()
	if request.method == "POST":
		form = CustomFormLayanan(data=request.POST)
		if request.POST.get('action') == "Hapus":
			id_layanan = get_object_or_404(KelolaLayanan, id=request.POST.get('id'))
			id_layanan.delete()
		else:
			if form.is_valid():
				if request.POST.get('action') == "Tambah":
					title = form.cleaned_data.get("title")
					content = form.cleaned_data.get("content")
					addLayanan = KelolaLayanan(title=title, content=content)
					addLayanan.save()
				elif request.POST.get('action') == "Edit":
					id_layanan = get_object_or_404(KelolaLayanan, id=request.POST.get('id'))
					form = CustomFormLayanan(data=request.POST, instance=id_layanan)
					form.save()
					
	return render(request, "admin/layanan.html", {'form':form})

def getLayanan(request):
	layanan = KelolaLayanan.objects.all().values('id','title','content')
	return JsonResponse(list(layanan), safe=False)
	