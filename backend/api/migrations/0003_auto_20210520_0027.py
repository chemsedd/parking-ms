# Generated by Django 3.2 on 2021-05-20 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210520_0019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lot',
            name='is_empty',
        ),
        migrations.AddField(
            model_name='lot',
            name='status',
            field=models.CharField(choices=[('E', 'Empty'), ('O', 'Occupied'), ('OUT', 'Out of service')], default='E', max_length=20),
        ),
        migrations.AlterField(
            model_name='lot',
            name='veh_type',
            field=models.CharField(choices=[('B', 'Bicycle'), ('BS', 'Bus'), ('C', 'Car'), ('CT', 'Consumer Truck'), ('M', 'Motorcycle'), ('T', 'Truck'), ('ST', 'Semi Truck'), ('V', 'Van')], default='C', max_length=20),
        ),
    ]
