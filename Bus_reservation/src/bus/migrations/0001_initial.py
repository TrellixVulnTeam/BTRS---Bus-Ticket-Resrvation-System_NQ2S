# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-09 05:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_number', models.IntegerField(default=50)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('type', models.CharField(choices=[(b'AC', b'AC Bus'), (b'NAC', b'Non AC bus')], default=b'AC', max_length=10)),
                ('arriving_time', models.TimeField()),
                ('depature_time', models.TimeField()),
                ('fare', models.DecimalField(decimal_places=2, max_digits=9)),
                ('no_of_seats', models.IntegerField(default=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=b'images/bus/main/')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'Bus',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'Route',
            },
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.Route')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'Stop',
            },
        ),
        migrations.AddField(
            model_name='bus',
            name='arriving_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pickuparea', to='bus.Stop'),
        ),
        migrations.AddField(
            model_name='bus',
            name='depature_at',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='droparea', to='bus.Stop'),
        ),
    ]
