from django.db import models

class KelolaLayanan(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=20)
	content = models.TextField()

	class Meta:
		db_table = 'tb_layanan'
