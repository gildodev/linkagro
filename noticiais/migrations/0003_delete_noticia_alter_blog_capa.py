# Generated by Django 5.1.6 on 2025-03-10 01:27

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticiais', '0002_blog'),
    ]

    operations = [
        
        migrations.AlterField(
            model_name='blog',
            name='capa',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='linkagro_noticiais/'),
        ),
    ]
