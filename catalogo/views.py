"""Vistas de la app catalogo."""
from django.shortcuts import render
from django.views.generic import ListView

from .models import Producto


# VISTA BASADA EN FUNCIÓN (FBV)
def home(request):
    """Página de bienvenida con un resumen del catálogo."""
    contexto = {
        "titulo": "Bienvenido",
        "total_productos": Producto.objects.count(),
        "total_categorias": Producto.objects.values("categoria").distinct().count(),
        "ultimos": Producto.objects.order_by("-creado_en")[:3],
    }
    return render(request, "home.html", contexto)


# VISTA BASADA EN CLASE (CBV)
class ProductoListView(ListView):
    """Catálogo ordenado por precio, con filtros opcionales por URL.

    /catalogo/                      -> todos los productos
    /catalogo/?categoria=Laptops    -> solo una categoría
    /catalogo/?stock=1              -> solo productos con stock
    """

    model = Producto
    template_name = "catalogo.html"
    context_object_name = "productos"

    def get_queryset(self):
        queryset = Producto.objects.order_by("precio")

        categoria = self.request.GET.get("categoria")
        if categoria:
            queryset = queryset.filter(categoria=categoria)

        if self.request.GET.get("stock") == "1":
            queryset = queryset.filter(stock__gt=0)

        return queryset

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["titulo"] = "Catálogo de Productos"
        contexto["categorias"] = (
            Producto.objects.order_by("categoria")
            .values_list("categoria", flat=True)
            .distinct()
        )
        contexto["categoria_actual"] = self.request.GET.get("categoria", "")
        contexto["solo_stock"] = self.request.GET.get("stock") == "1"
        return contexto
