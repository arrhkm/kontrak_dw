# Generated by Django 2.2.5 on 2019-09-20 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_group_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='employee',
        ),
        migrations.CreateModel(
            name='GroupEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employee.Employee')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employee.Group')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='employee',
            field=models.ManyToManyField(through='employee.GroupEmployee', to='employee.Employee'),
        ),
    ]