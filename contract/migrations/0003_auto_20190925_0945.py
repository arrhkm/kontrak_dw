# Generated by Django 2.2.5 on 2019-09-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0002_contract_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jabatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='contract',
            name='besar_upah',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
