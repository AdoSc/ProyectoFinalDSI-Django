from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models
from django import forms

# Create your models here.
# Clase de la tienda virtual para la base de datos de catálogos.
class Catalogo(models.Model):
    idnumcat = models.IntegerField(verbose_name="Nuevo número id del catálogo", default=0)
    titulo = models.CharField(max_length=200, verbose_name="Nombre del catálogo")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(verbose_name="Imagen del catálogo", upload_to="ProyectosImagenes")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha agregado")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha de última actualización")
    
    enlace = models.URLField(null=True, blank=True, max_length=200, )
    enlace = "/tienda/producto.html"

    class Meta:
        verbose_name = 'Catalogo'
        verbose_name_plural = 'Catalogos'
        ordering = ["-creado"]
    
    def __str__(self):
        return self.titulo
        
#Clase para agregar los productos a los catálogos en la base de datos.
class Producto(models.Model):
    idnumprod = models.IntegerField(verbose_name="Número id del catálogo al que será agregado", default=0)
    nombrep = models.CharField(max_length=200, verbose_name="Nombre del producto")
    detallep = models.TextField(verbose_name="Descripción")
    marcap = models.TextField(max_length=100, verbose_name="Marca del dispositivo", default="")
    imagenp = models.ImageField(verbose_name="Imagen del producto", upload_to="ProyectosImagenes")
    agregadop = models.DateTimeField(auto_now_add=True, verbose_name="Fecha agregado")
    modificadop = models.DateTimeField(auto_now=True, verbose_name="Fecha de última actualización")
    #menuCat = forms.ChoiceField(choices=Catalogo.titulo) #Para datos usados en esta misma app.
    #menuCat = forms.ModelChoiceField(queryset=Catalogo.objects.all()) #Para datos almacenados en una database
    #menuCat = forms.ChoiceField(label=Catalogo.objects.all()) #Para datos almacenados en una database

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ["-agregadop"]
    
    def __str__(self):
        return self.nombrep


