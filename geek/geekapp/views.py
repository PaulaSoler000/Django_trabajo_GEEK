from django.shortcuts import render, redirect
from .models import Inventario, Users, TipoObjeto
from .forms import InventarioForm, TipoObjetoForm

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso. Bienvenido!")
            return redirect(index_inventario)
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido de nuevo, {username}!")
                return redirect(index_inventario)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión exitosamente.")
    return redirect('login')

@login_required
def index_inventario(request):
    inventario = Inventario.objects.filter(id_usuario=request.user)
    return render(request, 'index_inventario.html', {'inventario': inventario})
# Inventario
""" def index_inventario(request):
    inventario = Inventario.objects.all()
    return render(request, 'index_inventario.html', {'inventario': inventario})
 """
 
def ver_inventario(request, id):
    inventario = Inventario.objects.get(id=id)
    return render(request, 'ver_inventario.html', {'inventario': inventario})

@login_required
def crear_inventario(request):
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index_inventario)
    else:
        form = InventarioForm()
    return render(request, 'crear_inventario.html', {'form': form})

def editar_inventario(request, id):
    inventario = Inventario.objects.get(id=id)
    if request.method == 'POST':
        form = InventarioForm(request.POST, instance=inventario)
        if form.is_valid():
            form.save()
            return redirect(index_inventario)
    else:
        form = InventarioForm(instance=inventario)
    return render(request, 'editar_inventario.html', {'form': form})

def eliminar_inventario(request, id):
    inventario = Inventario.objects.get(id=id)
    if request.method == 'POST' or request.method == 'DELETE':
        inventario.delete()
        return redirect(index_inventario)
    return render(request, 'eliminar_inventario.html', {'inventario': inventario})


# Users

""" def index_users(request):
    users = Users.objects.all()
    return render(request, 'index_users.html', {'users': users})

def ver_users(request, id):
    users = Users.objects.get(id=id)
    return render(request, 'ver_users.html', {'users': users})

def crear_users(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index_users)
    else:
        form = UsersForm()
    return render(request, 'crear_users.html', {'form': form})

def editar_users(request, id):
    users = Users.objects.get(id=id)
    if request.method == 'POST':
        form = UsersForm(request.POST, instance=users)
        if form.is_valid():
            form.save()
            return redirect(index_users)
    else:   
        form = UsersForm(instance=users)
    return render(request, 'editar_users.html', {'form': form})

def eliminar_users(request, id):
    users = Users.objects.get(id=id)
    if request.method == 'POST' or request.method == 'DELETE':
        users.delete()
        return redirect(index_users)
    return render(request, 'eliminar_users.html', {'users': users})

 """
# tipoObjeto	

def index_tipoObjeto(request):
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
    return render(request, 'eliminar_tipoObjeto.html', {'tipoObjeto': tipoObjeto})


