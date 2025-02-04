from django.shortcuts import render
from django.db import connection

def index(request):
	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM tb_mobil")
		result_mobil = cursor.fetchall()
		cursor.execute("SELECT * FROM tb_layanan")
		result_layanan = cursor.fetchall()

	context = {
		'mobil_list':result_mobil,
		'layanan_list': result_layanan,
	}
	return render(request, 'index/index.html', context)

def home_faq(request):
	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM tb_faq")
		result_faq = cursor.fetchall()

	context = {
		'faq_list': result_faq,
	}

	return render(request, 'index/faq.html', context)