from django import forms
from .models import Inventario, TipoObjeto
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['nombre_objeto', 'tipo_objeto', 'estado', 'curso', 'fecha_salida', 'descripcion', 'edicion', 'editorial', 'volumen', 'autor', 'precio', 'genero', 'altura', 'marca', 'plataforma', 'compania', 'cantidad', 'tags']
  
        
class TipoObjetoForm(forms.ModelForm):
    class Meta:
        model = TipoObjeto
        fields = ['tipo_objeto']

