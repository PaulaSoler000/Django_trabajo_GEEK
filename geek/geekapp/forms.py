from django import forms
from .models import Inventario, Users, TipoObjeto

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['nombre_objeto', 'id_tipoobjeto', 'estado', 'curso', 'fecha_salida', 'descripcion', 'edicion', 'editorial', 'volumen', 'autor', 'precio', 'genero', 'altura', 'marca', 'plataforma', 'compania', 'cantidad', 'tags']
  
        
class TipoObjetoForm(forms.ModelForm):
    class Meta:
        model = TipoObjeto
        fields = ['tipo_objeto']

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['usuario', 'email', 'password']

