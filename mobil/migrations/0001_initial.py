# Generated by Django 4.2.18 on 2025-01-27 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KelolaMobil',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('merek', models.CharField(max_length=50)),
                ('kapasitas', models.SmallIntegerField()),
                ('durasi', models.CharField(choices=[('Per Hari', 'Per Hari'), ('Per Minggu', 'Per Minggu'), ('Per Bulan', 'Per Bulan')], default='Per Hari', max_length=10)),
                ('harga', models.IntegerField()),
            ],
            options={
                'db_table': 'mobil',
            },
        ),
    ]
