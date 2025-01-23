from django.shortcuts import render

def mobil(request):
	return render(request, 'admin/mobil.html')

def artikel(request):
	return render(request, 'admin/artikel.html')