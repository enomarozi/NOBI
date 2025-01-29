from django.db import models

class KelolaMobil(models.Model):
	id = models.AutoField(primary_key=True)
	merek = models.CharField(max_length=50)
	kapasitas = models.SmallIntegerField()
	PERIODE_CHOICES = [
		('Harian','Harian'),
		('Mingguan','Mingguan'),
		('Bulanan','Bulanan'),
	]
	durasi = models.CharField(max_length=10, choices=PERIODE_CHOICES, default='Harian')
	harga = models.IntegerField()

	class Meta:
		db_table = 'tb_mobil'