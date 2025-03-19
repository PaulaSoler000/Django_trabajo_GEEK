# Generated by Django 5.1.7 on 2025-03-18 20:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geekapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='albums/images/')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='geekapp.inventario')),
            ],
        ),
    ]
