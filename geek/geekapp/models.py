from django.shortcuts import render
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager

class Inventario(models.Model):
    # Tu código actual...
    tags = TaggableManager()  # Reemplaza el campo CharField


class CustomUser(AbstractUser):
    # Agrega campos adicionales si los necesitas
    pass

""" class TipoObjeto(models.Model):
    tipo_objeto = models.CharField(max_length=100)
    
    def __str__(self):
        return self.tipo_objeto """


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
    
    TIPO_CHOICES = [
        ('libro', 'Libro'),
        ('manga', 'Manga'),
        ('comic', 'Cómic'),
        ('figura', 'Figura'),
        ('consola', 'Consola'),
        ('videojuego', 'Videojuego'),
        ('otro', 'Otro'),
    ]

    nombre_objeto = models.CharField(max_length=100)
    estado = models.CharField(
        max_length=12,
        choices=ESTADO_CHOICES
    )
    curso = models.CharField(
        max_length=12,
        choices=CURSO_CHOICES, 
        blank=True
    )
    
    tipo_objeto =models.CharField(
        max_length=12,
        choices=TIPO_CHOICES
    )
    
    fecha_salida = models.DateField(null=True, blank=True)
    #tags = models.CharField(max_length=100, null=True, blank=True)
    tags = TaggableManager(blank=True)
    descripcion = models.TextField(null=True, blank=True)
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
    

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nombre_objeto


class AlbumImage(models.Model):
    album = models.ForeignKey(Inventario, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='albums/images/')

    def __unicode__(self,):
        return str(self.image)