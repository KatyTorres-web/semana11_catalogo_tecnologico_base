"""Vistas de la app catalogo."""
from django.shortcuts import render
from django.views.generic import ListView

from .models import Producto


# VISTA BASADA EN FUNCIÓN (FBV)
def home(request):
    # TODO (compañera): contexto completo para la bienvenida
    return render(request, "home.html", {"titulo": "Bienvenido"})


# VISTA BASADA EN CLASE (CBV)
class ProductoListView(ListView):
    model = Producto
    template_name = "catalogo.html"
    # TODO (compañera): context_object_name, queryset filtrado y ordenado por precio
    # Ejemplo: queryset = Producto.objects.filter(stock__gt=0).order_by("precio")
