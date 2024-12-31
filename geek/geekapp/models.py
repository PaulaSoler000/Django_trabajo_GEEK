from django.shortcuts import render
from django.db import models

# Create your views here.
class Users(models.Model):
    usuario = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.usuario

class TipoObjeto(models.Model):
    tipo_objeto = models.CharField(max_length=100)
    
    def __str__(self):
        return self.tipo_objeto


class Inventario(models.Model):
    ESTADO_CHOICES = [
        ('nuevo', 'Nuevo'),
        ('bueno', 'Bueno'),
        ('malo', 'Malo'),
    ]
    
    CURSO_CHOICES = [
        ('sin_empezar', 'Sin empezar'),
        ('empezado', 'Empezado'),
        ('terminado', 'Terminado'),
    ]

    nombre_objeto = models.CharField(max_length=100)
    estado = models.CharField(
        max_length=12,
        choices=ESTADO_CHOICES,
        default='nuevo'
    )
    curso = models.CharField(
        max_length=12,
        choices=CURSO_CHOICES,
        default='sin_empezar'
    )
    fecha_salida = models.DateField(null=True, blank=True)
    tags = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    foto = models.CharField(max_length=200, null=True, blank=True)
    edicion = models.CharField(max_length=100, null=True, blank=True)
    editorial = models.CharField(max_length=100, null=True, blank=True)
    volumen = models.IntegerField(null=True, blank=True)
    autor = models.CharField(max_length=100, null=True, blank=True)
    genero = models.CharField(max_length=100, null=True, blank=True)
    altura = models.IntegerField(null=True, blank=True)
    marca = models.CharField(max_length=100, null=True, blank=True)
    plataforma = models.CharField(max_length=100, null=True, blank=True)
    compania = models.CharField(max_length=100, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True)
    
    id_usuario = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True)
    id_tipoobjeto = models.ForeignKey(TipoObjeto, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre_objeto

