from django.shortcuts import render

def artikel(request):
	return render(request, "admin/artikel.html")
