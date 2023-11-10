# Generated by Django 4.2.7 on 2023-11-10 15:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('currency', models.CharField(choices=[('USD', 'US Dollar'), ('AFG', 'Afghan Afghani')], max_length=3)),
                ('donation_type', models.CharField(choices=[('monthly', 'Monthly'), ('onetime', 'One-time')], max_length=10)),
                ('monthly_contribution', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(1)])),
                ('donation_duration_months', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]
