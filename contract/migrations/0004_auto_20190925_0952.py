# Generated by Django 2.2.5 on 2019-09-25 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0003_auto_20190925_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='jabatan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contract.Jabatan'),
        ),
    ]
