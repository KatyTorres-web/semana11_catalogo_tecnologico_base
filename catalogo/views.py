"""Vistas de la app catalogo."""
from django.shortcuts import render
from django.views.generic import ListView
from django.utils import timezone

from .models import Producto


# VISTA BASADA EN FUNCIÓN (FBV)
def home(request):
    contexto = {
        "titulo": "Tecnología para tu día a día",
        "descripcion": "Explora nuestro catálogo de productos tecnológicos y encuentra tu próximo equipo.",
        "total_productos": Producto.objects.count(),
        "total_categorias": Producto.objects.order_by().values("categoria").distinct().count(),
    }
    return render(request, "home.html", contexto)


# VISTA BASADA EN CLASE (CBV)
class ProductoListView(ListView):
    model = Producto
    template_name = "catalogo.html"
    context_object_name = "productos"
    def get_queryset(self):
        productos = Producto.objects.filter(precio__gt=0)
        categoria = self.request.GET.get("categoria", "")
        if categoria:
            productos = productos.filter(categoria=categoria)
        if self.request.GET.get("stock") == "1":
            productos = productos.filter(stock__gt=0)
        return productos.order_by("precio", "nombre")

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["titulo"] = "Explora nuestro catálogo"
        contexto["total_productos"] = contexto["productos"].count()
        contexto["fecha_consulta"] = timezone.localdate()
        contexto["categorias"] = Producto.objects.order_by("categoria").values_list("categoria", flat=True).distinct()
        contexto["categoria_actual"] = self.request.GET.get("categoria", "")
        contexto["solo_stock"] = self.request.GET.get("stock") == "1"
        return contexto
