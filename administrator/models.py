from django.db import models

class KelolaMobil(models.Model):
	id = models.AutoField(primary_key=True)
	merek = models.CharField(max_length=50)
	kapasitas = models.SmallIntegerField()
	PERIODE_CHOICES = [
		('Per Hari','Per Hari'),
		('Per Minggu','Per Minggu'),
		('Per Bulan', 'Per Bulan'),
	]
	durasi = models.CharField(max_length=10, choices=PERIODE_CHOICES, default='Per Hari')
	harga = models.IntegerField()

	class Meta:
		db_table = 'mobil'