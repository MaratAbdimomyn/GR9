# Generated by Django 4.2.2 on 2023-07-20 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=50)),
                ('c_aeroport_index', models.CharField(max_length=50)),
                ('c_car_number', models.CharField(max_length=50)),
            ],
        ),
    ]
