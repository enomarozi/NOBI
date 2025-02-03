from django.shortcuts import render
from django.db import connection

def index(request):
	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM tb_mobil")
		result = cursor.fetchall()

	return render(request, 'index/index.html', {'mobil_list':result})