# Generated by Django 5.1.7 on 2025-03-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geekapp', '0006_alter_inventario_curso_alter_inventario_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='curso',
            field=models.CharField(choices=[('', '---------'), ('sin_empezar', 'Sin empezar'), ('empezado', 'Empezado'), ('terminado', 'Terminado')], max_length=12),
        ),
    ]
