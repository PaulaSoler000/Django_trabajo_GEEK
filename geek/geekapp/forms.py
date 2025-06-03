from django import forms
from .models import Inventario, AlbumImage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from taggit.forms import TagWidget

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
        fields = ['nombre_objeto', 'tipo_objeto', 'estado', 'curso', 'fecha_salida','fecha_compra', 'descripcion', 'edicion', 'editorial', 'volumen', 'autor', 'precio', 'genero', 'altura', 'marca', 'plataforma', 'compania', 'cantidad', 'tags']
        widgets = {
            'tags': TagWidget(attrs={'placeholder': 'Escribe los tags separados por comas'}),}

    def clean_tags(self):
        tags = self.cleaned_data['tags']
        # Si el usuario escribe los tags como texto, conviértelos a lista
        if hasattr(tags, 'all'):
            tags_list = list(tags.all())
        else:
            tags_list = list(tags)
        if len(tags_list) > 5:
            raise forms.ValidationError("No puedes añadir más de 5 tags.")
        return tags
        
class UploadImageForm(forms.ModelForm):

    class Meta:
        model = AlbumImage
        fields = ['image']
        
""" class TipoObjetoForm(forms.ModelForm):
    class Meta:
        model = TipoObjeto
        fields = ['tipo_objeto'] """

