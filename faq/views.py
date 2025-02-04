from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .forms import CustomFormFAQ
from .models import KelolaFAQ


def FAQ(request):
	form = CustomFormFAQ()
	if request.method == "POST":
		form = CustomFormFAQ(data=request.POST)
		if request.POST.get('action') == "Hapus":
			id_faq = get_object_or_404(KelolaFAQ, id=request.POST.get('id'))
			id_faq.delete()
			messages.success(request,"Hapus Record Berhasil.")
		else:
			if form.is_valid():
				if request.POST.get('action') == "Tambah":
					pertanyaan = form.cleaned_data.get("pertanyaan")
					jawaban = form.cleaned_data.get("jawaban")
					addFAQ = KelolaFAQ(pertanyaan=pertanyaan, jawaban=jawaban)
					addFAQ.save()
					messages.success(request,"Tambah Record Berhasil.")
				elif request.POST.get('action') == "Edit":
					id_faq = get_object_or_404(KelolaFAQ, id=request.POST.get('id'))
					form = CustomFormFAQ(data=request.POST, instance=id_faq)
					form.save()
					messages.success(request,"Edit Record Berhasil.")
					
	return render(request, "admin/faq.html", {'form':form})

def getFAQ(request):
	faq_data = KelolaFAQ.objects.all().values('id','pertanyaan','jawaban')
	return JsonResponse(list(faq_data), safe=False)