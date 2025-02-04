from django.db import models

class KelolaMobil(models.Model):
	id = models.AutoField(primary_key=True)
	filename = models.CharField(max_length=100, null=True, blank=True)
	merek = models.CharField(max_length=50)
	kapasitas = models.SmallIntegerField()
	PERIODE_CHOICES = [
		('Harian','Harian'),
		('Mingguan','Mingguan'),
		('Bulanan','Bulanan'),
	]
	durasi = models.CharField(max_length=50, choices=PERIODE_CHOICES, default='Harian')
	harga = models.IntegerField()

	class Meta:
		db_table = 'tb_mobil'