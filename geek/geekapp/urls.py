from django.contrib import admin
from django.urls import path, include
from .views import login_view, index_inventario, register_view, crear_inventario, ver_inventario, eliminar_inventario, editar_inventario, logout_view, buscar_inventario

urlpatterns = [
    
    path('', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('inventario/', index_inventario, name='inventario'),
    path('crear_inventario/', crear_inventario, name='crear_inventario'),
    path('ver_inventario/<int:id>', ver_inventario, name='ver_inventario'),
    path('editar_inventario/<int:id>', editar_inventario, name='editar_inventario'),
    path('eliminar_inventario/<int:id>', eliminar_inventario, name='eliminar_inventario'),
    path('logout/', logout_view, name='logout'),
    path('buscar_inventario/', buscar_inventario, name='buscar_inventario'),
    
]
