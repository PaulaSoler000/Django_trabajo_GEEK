from django import forms
from .models import Inventario, Users, Galeria

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['nombre_objeto', 'id_tipoobjeto', 'estado', 'curso', 'fecha_salida', 'descripcion', 'edicion', 'editorial', 'volumen', 'autor', 'precio', 'genero', 'altura', 'marca', 'plataforma', 'compania', 'cantidad','galeria', 'tags']
        widgets = {
            'galeria': forms.URLInput(attrs={'placeholder': 'Ingrese la URL de la imagen'}),
        }

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['usuario', 'email', 'password']

class GaleriaForm(forms.ModelForm):
    class Meta:
        model = Galeria
        fields = ['galeria']
        widgets = {
            'galeria': forms.URLInput(attrs={'placeholder': 'Ingrese la URL de la imagen'}),
        }