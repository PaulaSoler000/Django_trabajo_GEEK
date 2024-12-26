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
    fecha_salida = models.DateField()
    tags = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.CharField(max_length=200)
    edicion = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    volumen = models.IntegerField()
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    altura = models.IntegerField()
    marca = models.CharField(max_length=100)
    plataforma = models.CharField(max_length=100)
    compania = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    
    id_usuario = models.ForeignKey(Users, on_delete=models.CASCADE)
    id_tipoobjeto = models.ForeignKey(TipoObjeto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_objeto

class Galeria(models.Model):
    id_inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    galeria = models.CharField(max_length=200)
    
    def __str__(self):
        return self.galeria