# Generated by Django 5.0.6 on 2025-01-18 10:17

import phone_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=31)),
                ('last_name', models.CharField(max_length=31)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
