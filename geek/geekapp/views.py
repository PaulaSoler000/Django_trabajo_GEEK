from django.shortcuts import render, redirect
from .models import Inventario, CustomUser, AlbumImage
from .forms import InventarioForm, CustomUserCreationForm, CustomAuthenticationForm, UploadImageForm
from django.shortcuts import render
from taggit.models import Tag
from django.http import JsonResponse

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory, modelformset_factory

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso. Bienvenido!")
            return redirect(index_inventario)
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido de nuevo, {username}!")
                return redirect(index_inventario)
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión exitosamente.")
    return redirect(login_view)


""" @login_required
def index_inventario(request):
    inventario = Inventario.objects.filter(usuario=request.user)
    return render(request, 'index_inventario.html', {'inventario': inventario})
 """
 
""" @login_required
def index_inventario(request):
    tipo_objeto_filtro = request.GET.get('tipo_objeto', '')  # Obtiene el filtro desde la URL
    inventario = Inventario.objects.filter(usuario=request.user)

    if tipo_objeto_filtro:
        inventario = inventario.filter(tipo_objeto=tipo_objeto_filtro)

    return render(request, 'index_inventario.html', {
        'inventario': inventario,
        'tipo_objeto_filtro': tipo_objeto_filtro,
        'TIPO_CHOICES': Inventario.TIPO_CHOICES,  # Para generar las opciones en la plantilla
    }) """

def buscar_inventario(request):
    query = request.GET.get('search', '')  # Capturar el término de búsqueda
    if query:
        inventario = Inventario.objects.filter(nombre_objeto__icontains=query)  # Filtrar por nombre
    else:
        inventario = Inventario.objects.all()  # Mostrar todo si no hay búsqueda

    # Devolver los resultados en formato JSON
    return JsonResponse({'inventario': list(inventario.values('id', 'nombre_objeto'))})

""" @login_required
def index_inventario(request):
    tipo_objeto_filtro = request.GET.get('tipo_objeto', '')  # Obtiene el filtro de tipo de objeto
    tag_filtro = request.GET.get('tag', '')  # Obtiene el filtro de tag
    inventario = Inventario.objects.filter(usuario=request.user)

    # Filtrar por tipo de objeto
    if tipo_objeto_filtro:
        inventario = inventario.filter(tipo_objeto=tipo_objeto_filtro)

    # Filtrar por tag
    if tag_filtro:
        inventario = inventario.filter(tags__name=tag_filtro)  # Filtra por el nombre del tag

    # Obtener todos los tags disponibles para mostrarlos en el formulario
    tags_disponibles = Tag.objects.all()

    return render(request, 'index_inventario.html', {
        'inventario': inventario,
        'tipo_objeto_filtro': tipo_objeto_filtro,
        'tag_filtro': tag_filtro,
        'TIPO_CHOICES': Inventario.TIPO_CHOICES,  # Para generar las opciones en la plantilla
        'tags_disponibles': tags_disponibles,  # Pasa los tags disponibles al template
    }) """

@login_required
def index_inventario(request):
    # Capturar parámetros de búsqueda y filtros
    query = request.GET.get('search', '')  # Nuevo parámetro de búsqueda
    tipo_objeto_filtro = request.GET.get('tipo_objeto', '')
    tag_filtro = request.GET.get('tag', '')
    estado_filtro = request.GET.get('estado', '')
    precio_orden = request.GET.get('precio_orden', '')

    inventario = Inventario.objects.filter(usuario=request.user)

    # Aplicar búsqueda por nombre
    if query:
        inventario = inventario.filter(nombre_objeto__icontains=query)  # Filtra por nombre

    # Resto de filtros (mantén tu lógica existente)
    if tipo_objeto_filtro:
        inventario = inventario.filter(tipo_objeto=tipo_objeto_filtro)
    
    if tag_filtro:
        inventario = inventario.filter(tags__name=tag_filtro)
    
    if estado_filtro:
        inventario = inventario.filter(estado=estado_filtro)

    # Ordenar por precio
    if precio_orden == 'asc':
        inventario = inventario.order_by('precio')
    elif precio_orden == 'desc':
        inventario = inventario.order_by('-precio')
    tags_disponibles = Tag.objects.all()

    return render(request, 'index_inventario.html', {
        'inventario': inventario,
        'tipo_objeto_filtro': tipo_objeto_filtro,
        'tag_filtro': tag_filtro,
        'estado_filtro': estado_filtro,
        'precio_orden': precio_orden,
        'TIPO_CHOICES': Inventario.TIPO_CHOICES,
        'tags_disponibles': tags_disponibles,
        'ESTADO_CHOICES': Inventario.ESTADO_CHOICES,  # Para el filtro de estado
    })



# Inventario

""" def ver_inventario(request, id):
    inventario = Inventario.objects.get(id=id)
    return render(request, 'ver_inventario.html', {'inventario': inventario})
 """
def ver_inventario(request, id):
    inventario = Inventario.objects.get(id=id)
    imagenes = AlbumImage.objects.filter(album=inventario)
    return render(request, 'ver_inventario.html', {'inventario': inventario, 'imagenes': imagenes})

 
""" @login_required
def crear_inventario(request):
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index_inventario)
    else:
        form = InventarioForm()
    return render(request, 'crear_inventario.html', {'form': form}) """
""" 
@login_required
def crear_inventario(request):
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            inventario = form.save(commit=False)
            inventario.usuario = request.user
            inventario.save()
            return redirect(index_inventario)
    else:
        form = InventarioForm()
    return render(request, 'crear_inventario.html', {'form': form})
 """

def crear_inventario(request):
    ImageFormSet = formset_factory(UploadImageForm, extra=4)  # Permite subir hasta 4 imágenes

    if request.method == 'POST':
        inventario_form = InventarioForm(request.POST)
        image_formset = ImageFormSet(request.POST, request.FILES)

        if inventario_form.is_valid() and image_formset.is_valid():
            inventario = inventario_form.save(commit=False)
            inventario.usuario = request.user
            inventario.save()
            
            # ¡IMPORTANTE! Guardar los tags después de guardar el objeto principal
            inventario_form.save_m2m()  # Esto guarda las relaciones many-to-many (como los tags)
            
            # Guardar las imágenes
            for image_form in image_formset:
                if image_form.cleaned_data.get('image'):
                    image = image_form.save(commit=False)
                    image.album = inventario
                    image.save()

            return redirect('inventario')
    else:
        inventario_form = InventarioForm()
        image_formset = ImageFormSet()
    
    return render(request, 'crear_inventario.html', {
        'inventario_form': inventario_form,
        'image_formset': image_formset
    })

""" @login_required
def upload_image_view(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Image uploaded succesfully!"
    else:
        form = UploadImageForm()

    return render('albums/upload.html', locals(), context_instance=RequestContext(request))
 """

""" def editar_inventario(request, id):
    inventario = get_object_or_404(Inventario, id=id)
    
    # Creamos un formset con exactamente 4 formularios (uno por cada imagen que queremos mostrar siempre)
    ImageFormSet = modelformset_factory(AlbumImage, form=UploadImageForm, extra=0, max_num=4)
    
    # Obtenemos las imágenes existentes del inventario
    existing_images = inventario.images.all()
    
    # Si hay menos de 4 imágenes, agregamos formularios vacíos hasta completar los 4
    empty_forms_needed = 4 - existing_images.count()
    
    if request.method == 'POST':
        form = InventarioForm(request.POST, instance=inventario)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=existing_images)
        
        if form.is_valid() and image_formset.is_valid():
            form.save()
            
            # Guardar imágenes nuevas reemplazando las antiguas
            for form in image_formset:
                if form.cleaned_data.get('image'):  # Solo guardar si hay imagen
                    image = form.save(commit=False)
                    image.album = inventario
                    image.save()
                    
            return redirect('inventario')
    else:
        form = InventarioForm(instance=inventario)
        image_formset = ImageFormSet(queryset=existing_images)

    return render(request, 'editar_inventario.html', {
        'form': form,
        'image_formset': image_formset,
        'empty_forms_needed': range(empty_forms_needed)  # Para renderizar formularios vacíos en la plantilla
    })
     """
     
     
""" def editar_inventario(request, id):
    inventario = get_object_or_404(Inventario, id=id)

    # Permitir hasta 4 imágenes en total (existentes + nuevas)
    ImageFormSet = modelformset_factory(AlbumImage, form=UploadImageForm, extra=4, max_num=4, can_delete=True)

    existing_images = inventario.images.all()
    
    if request.method == 'POST':
        form = InventarioForm(request.POST, instance=inventario)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=existing_images)

        if form.is_valid() and image_formset.is_valid():
            form.save()
            
            for image_form in image_formset:
                if image_form.cleaned_data.get('image'):  # Solo guardar si hay imagen
                    image = image_form.save(commit=False)
                    image.album = inventario  # Asociar la imagen con el inventario
                    image.save()
                
                if image_form.cleaned_data.get('DELETE'):  # Eliminar imagen si el usuario lo indica
                    image_form.instance.delete()
            
            return redirect('inventario')
    
    else:
        form = InventarioForm(instance=inventario)
        image_formset = ImageFormSet(queryset=existing_images)

    return render(request, 'editar_inventario.html', {
        'form': form,
        'image_formset': image_formset
    }) """

def editar_inventario(request, id):
    inventario = get_object_or_404(Inventario, id=id)
    ImageFormSet = modelformset_factory(AlbumImage, form=UploadImageForm, extra=4, max_num=4, can_delete=True)
    existing_images = inventario.images.all()

    if request.method == 'POST':
        form = InventarioForm(request.POST, instance=inventario)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=existing_images)

        if form.is_valid() and image_formset.is_valid():
            inventario = form.save()
            # Actualiza los tags (django-taggit)
            inventario.tags.set(form.cleaned_data['tags'])

            # Guardar imágenes nuevas y eliminar las marcadas para borrar
            instances = image_formset.save(commit=False)
            for instance in instances:
                instance.album = inventario
                instance.save()
            for obj in image_formset.deleted_objects:
                obj.delete()

            # ELIMINAR TAGS HUÉRFANOS DESPUÉS DE EDITAR
            Tag.objects.filter(taggit_taggeditem_items__isnull=True).delete()

            return redirect('inventario')
    else:
        form = InventarioForm(instance=inventario)
        image_formset = ImageFormSet(queryset=existing_images)

    return render(request, 'editar_inventario.html', {
        'form': form,
        'image_formset': image_formset,
        'inventario': inventario,
    })
    
""" def editar_inventario(request, id):
    inventario = Inventario.objects.get(id=id)
    if request.method == 'POST':
        form = InventarioForm(request.POST, instance=inventario)
        if form.is_valid():
            form.save()
            return redirect(index_inventario)
    else:
        form = InventarioForm(instance=inventario)
    return render(request, 'editar_inventario.html', {'form': form})
 """
 
 
 
 
""" def eliminar_inventario(request, id):
    inventario = Inventario.objects.get(id=id)
    if request.method == 'POST' or request.method == 'DELETE':
        inventario.delete()
        return redirect(index_inventario)
    return render(request, 'eliminar_inventario.html', {'inventario': inventario})
 """

def eliminar_inventario(request, id):
    inventario = Inventario.objects.get(id=id)
    if request.method == 'POST' or request.method == 'DELETE':
        # Guardamos los tags asociados antes de eliminar
        tags_asociados = list(inventario.tags.all())
        
        inventario.delete()
        
        # Verificamos si los tags quedaron sin uso
        for tag in tags_asociados:
            if tag.taggit_taggeditem_items.count() == 0:
                tag.delete()
                
        return redirect(index_inventario)
    return render(request, 'eliminar_inventario.html', {'inventario': inventario})

# tipoObjeto	

""" def index_tipoObjeto(request):
    tipoObjeto = TipoObjeto.objects.all()
    return render(request, 'index_tipoObjeto.html', {'tipoObjeto': tipoObjeto})

def ver_tipoObjeto(request, id):
    tipoObjeto = TipoObjeto.objects.get(id=id)
    return render(request, 'ver_tipoObjeto.html', {'tipoObjeto': tipoObjeto})

def crear_tipoObjeto(request):
    if request.method == 'POST':
        form = TipoObjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index_tipoObjeto)
    else:
        form = TipoObjetoForm()
    return render(request, 'crear_tipoObjeto.html', {'form': form})

def editar_tipoObjeto(request, id):
    tipoObjeto = TipoObjeto.objects.get(id=id)
    if request.method == 'POST':
        form = TipoObjetoForm(request.POST, instance=tipoObjeto)
        if form.is_valid():
            form.save()
            return redirect(index_tipoObjeto)
    else:
        form = TipoObjetoForm(instance=tipoObjeto)
    return render(request, 'editar_tipoObjeto.html', {'form': form})

def eliminar_tipoObjeto(request, id):
    tipoObjeto = TipoObjeto.objects.get(id=id)
    if request.method == 'POST' or request.method == 'DELETE':
        tipoObjeto.delete()
        return redirect(index_tipoObjeto)
    return render(request, 'eliminar_tipoObjeto.html', {'tipoObjeto': tipoObjeto}) """


