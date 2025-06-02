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
from django.core.paginator import Paginator

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



@login_required
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
 """

@login_required
def index_inventario(request):
    # Capturar parámetros de búsqueda y filtros
    query = request.GET.get('search', '')
    tipo_objeto_filtro = request.GET.get('tipo_objeto', '')
    tag_filtro = request.GET.get('tag', '')
    estado_filtro = request.GET.get('estado', '')
    precio_orden = request.GET.get('precio_orden', '')

    inventario = Inventario.objects.filter(usuario=request.user)

    if query:
        inventario = inventario.filter(nombre_objeto__icontains=query)
    if tipo_objeto_filtro:
        inventario = inventario.filter(tipo_objeto=tipo_objeto_filtro)
    if tag_filtro:
        inventario = inventario.filter(tags__name=tag_filtro)
    if estado_filtro:
        inventario = inventario.filter(estado=estado_filtro)
    if precio_orden == 'asc':
        inventario = inventario.order_by('precio')
    elif precio_orden == 'desc':
        inventario = inventario.order_by('-precio')

    tags_disponibles = Tag.objects.all()

    # PAGINACIÓN
    paginator = Paginator(inventario, 20)  # 20 por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index_inventario.html', {
        'page_obj': page_obj,  # Usar esto en el template
        'tipo_objeto_filtro': tipo_objeto_filtro,
        'tag_filtro': tag_filtro,
        'estado_filtro': estado_filtro,
        'precio_orden': precio_orden,
        'TIPO_CHOICES': Inventario.TIPO_CHOICES,
        'tags_disponibles': tags_disponibles,
        'ESTADO_CHOICES': Inventario.ESTADO_CHOICES,
        'is_paginated': page_obj.has_other_pages(),
        'paginator': paginator,
        'request': request,  # Para mantener los filtros en la paginación
    })


# Inventario


@login_required 
def ver_inventario(request, id):
    inventario = Inventario.objects.get(id=id)
    imagenes = AlbumImage.objects.filter(album=inventario)
    return render(request, 'ver_inventario.html', {'inventario': inventario, 'imagenes': imagenes})


@login_required
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

    
@login_required
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
    


@login_required
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

