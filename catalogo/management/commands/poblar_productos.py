"""Carga productos tecnológicos de ejemplo.

Uso:  python manage.py poblar_productos
Se puede ejecutar varias veces: no duplica (usa update_or_create).
"""
from decimal import Decimal

from django.core.management.base import BaseCommand

from catalogo.models import Producto

PRODUCTOS = [
    ("laptop lenovo ideapad 3", "1899.00", "Laptops", 12),
    ("laptop asus vivobook 15", "2299.90", "Laptops", 0),
    ("smartphone samsung galaxy a55", "1499.00", "Smartphones", 25),
    ("smartphone xiaomi redmi note 13", "899.00", "Smartphones", 40),
    ("audífonos sony wh-ch520", "229.90", "Audio", 18),
    ("parlante jbl flip 6", "449.00", "Audio", 0),
    ("monitor lg 24 pulgadas ips", "599.00", "Monitores", 9),
    ("mouse logitech m185", "49.90", "Accesorios", 60),
    ("teclado mecánico redragon kumara", "159.00", "Accesorios", 15),
    ("disco ssd kingston 1tb", "289.00", "Almacenamiento", 30),
]


class Command(BaseCommand):
    help = "Carga productos tecnológicos de ejemplo"

    def handle(self, *args, **options):
        creados = 0
        for nombre, precio, categoria, stock in PRODUCTOS:
            _, creado = Producto.objects.update_or_create(
                nombre=nombre,
                defaults={"precio": Decimal(precio), "categoria": categoria, "stock": stock},
            )
            creados += creado
        self.stdout.write(self.style.SUCCESS(
            f"[OK] {creados} producto(s) creado(s). Total: {Producto.objects.count()}"
        ))
