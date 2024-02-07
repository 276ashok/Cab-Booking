# Generated by Django 5.0.1 on 2024-01-30 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('account', models.CharField(default='0', max_length=16)),
                ('contact', models.CharField(default='', max_length=16)),
                ('address', models.CharField(default='', max_length=100)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Taxi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.CharField(default='0', max_length=15)),
                ('total_seats', models.IntegerField(default='4')),
                ('taxi_type', models.CharField(choices=[('SUV', 'SUV'), ('SEDAN', 'Sedan'), ('VAN', 'Van'), ('ELECTRIC', 'Electric'), ('BIKE', 'Bike')], max_length=20)),
                ('fair_ratio', models.IntegerField(default=10)),
                ('taxi_info', models.CharField(max_length=200, null=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]