from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models
from django.db.models import Count
from autoslug import AutoSlugField
from decimal import Decimal

# Clase de la tienda virtual para la base de datos de categorías.
class Categoria(models.Model):
    idnumcat = models.IntegerField(primary_key=True, verbose_name="Id de la categoría")
    titulo = models.CharField(max_length=200, verbose_name="Nombre de la categoría")
    slug = AutoSlugField(populate_from='titulo')
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(verbose_name="Imagen de la categoría", upload_to="ProyectosImagenes")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha agregado")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha de última actualización")

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ["-creado"]
    
    def __str__(self):
        return self.titulo

#Clase para agregar los productos a las categorias en la base de datos.
class Producto(models.Model):
    idnumprod = models.IntegerField(primary_key=True, verbose_name="Id del producto")
    cantidadp = models.IntegerField(verbose_name="Cantidad disponible", default=1)
    nombrep = models.CharField(max_length=200, verbose_name="Nombre del producto")
    slug = AutoSlugField(populate_from='nombrep')
    detallep = models.TextField(verbose_name="Descripción")
    marcap = models.CharField(max_length=100, verbose_name="Marca del producto")
    preciop = models.DecimalField(max_digits=15, decimal_places=2, default=0.0, verbose_name="Precio del producto")
    idnumcatp = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Disponible en categoría")
    imagenp = models.ImageField(verbose_name="Imagen del producto", upload_to="ProyectosImagenes")
    agregadop = models.DateTimeField(auto_now_add=True, verbose_name="Fecha agregado")
    modificadop = models.DateTimeField(auto_now=True, verbose_name="Fecha de última modificación")

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ["-agregadop"]
    
    def __str__(self):
        return self.nombrep



