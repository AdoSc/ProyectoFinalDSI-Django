from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Categoria
from .models import Producto

# Create your views here.
class VistaListaCategoria(ListView):
    model = Categoria

#Método para devolver la lista de Categorias.
#def Tienda(request):
#    categoriasweb = Categoria.objects.all()
#    return render(request, "tienda/tienda.html", {'categoriasweb': categoriasweb}) # Envía la dirección del código.

#Método para devolver la lista de productos.
class VistaListaProducto(ListView):
    model = Producto

#No funciona aún, debería reemplazar a la función de arriba. Revisar el importe en urls.py y nombre del archivo.html.
#class VistaDetalleProducto(DetailView):
#    model = Producto

#def TiendaProducto(request):
#    productosweb = Producto.objects.all()
#    """
#    if Categoria.enlace[-1]=="/" | Categoria.enlace[-1]=="":
#        productosweb = Producto.objects.all()
#    else:
#        productosweb = Producto.objects.filter(idnumcatp=1)
#        """
#    return render(request, "tienda/producto.html", {'productosweb': productosweb})

def FiltrarProductos(request, slug):
    catFiltrada=Categoria.objects.get(slug=slug)
    productosFiltrados =Producto.objects.filter(idnumcatp=catFiltrada)
    return render(request, "tienda/FiltrarProductos.html", {'productosFiltrados': productosFiltrados})
