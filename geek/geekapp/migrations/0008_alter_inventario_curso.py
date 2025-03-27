# Generated by Django 5.1.7 on 2025-03-27 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geekapp', '0007_alter_inventario_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='curso',
            field=models.CharField(blank=True, choices=[('', '---------'), ('sin_empezar', 'Sin empezar'), ('empezado', 'Empezado'), ('terminado', 'Terminado')], max_length=12),
        ),
    ]
