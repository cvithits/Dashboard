# Generated by Django 2.1.1 on 2018-09-24 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEOD_Mon', '0002_auto_20180924_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='log_info',
            field=models.CharField(blank=True, max_length=200, verbose_name='Log'),
        ),
    ]
