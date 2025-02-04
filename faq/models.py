from django.db import models

class KelolaFAQ(models.Model):
	id = models.AutoField(primary_key=True)
	pertanyaan = models.CharField(max_length=255)
	jawaban = models.TextField()

	class Meta:
		db_table = 'tb_faq'