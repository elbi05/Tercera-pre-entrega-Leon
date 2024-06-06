from django.contrib import admin
from django.urls import path, include
from AppCafe.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('cliente/',cliente,name="Cliente"),
    path('mesero/',mesero,name="Mesero"),
    path('cuenta/',cuenta,name="Cuenta"),
    path('buscar/',buscar,name="Buscar"),
    path('busquedaMesa/',busquedaMesa, name="BusquedaMesa"),
]