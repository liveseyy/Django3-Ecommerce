# Generated by Django 3.1.4 on 2020-12-25 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20201225_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='sd_volume_max',
            field=models.CharField(blank=True, max_length=255, verbose_name='Максимальный объём встраиваемой памяти'),
        ),
    ]
