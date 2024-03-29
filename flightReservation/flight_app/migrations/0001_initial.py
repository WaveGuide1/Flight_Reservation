# Generated by Django 5.0.1 on 2024-01-11 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operating_airline', models.CharField(max_length=225)),
                ('flight_number', models.CharField(max_length=225)),
                ('arrival_country', models.CharField(max_length=225)),
                ('departure_country', models.CharField(max_length=225)),
                ('operation_date', models.DateField()),
                ('time_departure', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flight_app.passenger')),
                ('passenger', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flight_app.flight')),
            ],
        ),
    ]
