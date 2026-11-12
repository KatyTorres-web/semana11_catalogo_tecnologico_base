"""Modelos de la app catalogo."""
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Producto(models.Model):
    """Producto tecnológico del catálogo."""

    class Categoria(models.TextChoices):
        LAPTOPS = "Laptops", "Laptops"
        SMARTPHONES = "Smartphones", "Smartphones"
        AUDIO = "Audio", "Audio"
        MONITORES = "Monitores", "Monitores"
        ACCESORIOS = "Accesorios", "Accesorios"
        ALMACENAMIENTO = "Almacenamiento", "Almacenamiento"

    nombre = models.CharField("nombre", max_length=100)
    precio = models.DecimalField(
        "precio (S/)",
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
    )
    categoria = models.CharField("categoría", max_length=50, choices=Categoria.choices)
    stock = models.PositiveIntegerField("stock", default=0)
    creado_en = models.DateTimeField("creado en", auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-creado_en"]

    def __str__(self):
        """Representación legible en el admin y en la consola (shell)."""
        estado = "agotado" if self.stock == 0 else f"{self.stock} en stock"
        return f"{self.nombre.title()} - S/ {self.precio} ({estado})"
