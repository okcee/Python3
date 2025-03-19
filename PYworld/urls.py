# PYworld/urls.py
from django.urls import path
from . import views  # Aquí el '.' se refiere al directorio actual de la aplicación PYworld

urlpatterns = [
    path('inicio/', views.mi_vista_inicio, name='inicio'),
    path('otro/', views.otra_vista, name='otra'),
    # ... otras rutas de la aplicación PYworld
]