# Generated by Django 2.2.5 on 2019-09-25 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0004_auto_20190925_0952'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jabatan',
            options={'verbose_name_plural': 'Jabatan'},
        ),
        migrations.AlterField(
            model_name='contract',
            name='doc_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
