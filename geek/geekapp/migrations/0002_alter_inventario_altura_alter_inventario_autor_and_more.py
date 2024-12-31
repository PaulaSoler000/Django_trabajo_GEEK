# Generated by Django 5.1.4 on 2024-12-31 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geekapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='altura',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='autor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='compania',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='edicion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='editorial',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='fecha_salida',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='foto',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='genero',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='id_tipoobjeto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geekapp.tipoobjeto'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='id_usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geekapp.users'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='marca',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='plataforma',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='tags',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='volumen',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Galeria',
        ),
    ]
