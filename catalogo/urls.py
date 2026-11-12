"""Rutas de la app catalogo."""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),                                    # FBV
    path("catalogo/", views.ProductoListView.as_view(), name="catalogo"),  # CBV
]
