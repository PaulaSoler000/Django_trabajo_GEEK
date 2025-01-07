from django.contrib import admin
from django.urls import path, include
from .views import login_view, index_inventario, register_view, crear_inventario

urlpatterns = [
    
    path('', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('inventario/', index_inventario, name='inventario'),
    path('crear_inventario/', crear_inventario, name='crear_inventario'),
]
