from django.shortcuts import render
from .models import Catalogo
from .models import Producto

# Create your views here.
#Método para devolver la lista de catálogos.
def Tienda(request):
    catalogosweb = Catalogo.objects.all()
    return render(request, "tienda/tienda.html", {'catalogosweb': catalogosweb}) # Envía la dirección del código.

#Método para devolver la lista de productos.
def TiendaProducto(request):
    productosweb = Producto.objects.all()
    return render(request, "tienda/producto.html", {'productosweb': productosweb})

#No utilizado, se puede borrar luego.
temp = 0

def CATEMP(t):
    temp = t

def CATEMP():
    return temp
