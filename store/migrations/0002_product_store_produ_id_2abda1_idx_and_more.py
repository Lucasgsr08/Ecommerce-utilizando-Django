# Generated by Django 5.2.3 on 2025-06-18 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['id', 'slug'], name='store_produ_id_2abda1_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['name'], name='store_produ_name_5e57da_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['-created'], name='store_produ_created_ca958a_idx'),
        ),
    ]
