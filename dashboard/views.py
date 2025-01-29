from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.db import connection


def dashboard(request):
	if request.user.is_authenticated:
		with connection.cursor() as cursor:
			cursor.execute("SELECT COUNT(*) FROM tb_mobil")
			mobil_count = cursor.fetchone()[0]
			cursor.execute("SELECT COUNT(*) FROM tb_layanan")
			layanan_count = cursor.fetchone()[0]
		context = {
			'mobil':mobil_count,
			'layanan':layanan_count,
		}
		print(context)
		return render(request, 'admin/dashboard.html',context)
	return HttpResponseRedirect(reverse('signin'))