from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from .models import Categoria
from .models import Producto

# Create your views here.
class VistaListaCategoria(ListView):
    model = Categoria
    
    

class VistaListaProducto(ListView):
    model = Producto



def FiltrarProductos(request, slug):
    catFiltrada=Categoria.objects.get(slug=slug)
    productosFiltrados =Producto.objects.filter(idnumcatp=catFiltrada)
    return render(request, "tienda/FiltrarProductos.html", {'productosFiltrados': productosFiltrados})

#--------------nuevas vistas---------#

def Detalle(request, slug):
    catFiltrada2=Producto.objects.get(slug=slug)
    
    return render(request, "tienda/detalles.html", {'catFiltrada2': catFiltrada2})

def Cart(request, slug):
    product=Producto.objects.get(slug=slug)
    
    agregar = {"item":[], "precio":0.0, "contador":0}
    session = request.session.get("data", agregar)
    session["item"].append(slug)
    session["precio"] += float(product.preciop)
    session["contador"] += 1
    messages.success(request,"Agregado a la lista!")
    request.session["data"]=session
    
    return redirect("detail", slug)

def Mycart (request):
    sess=request.session.get("data",{"item":[]})
    myproducts=Producto.objects.filter(slug__in=sess["item"])
    return render(request, "tienda/micarrito.html", {'myproducts':myproducts})

#vista para reiniciar los objetos seleccionados osea al hacer la compra
def Comprar (request):
    sessdel=request.session.get("data", {"item":[]})
    del request.session["data"]
    return redirect("Mycart")

#Re-definido para borrar la lista de compras.
def BorrarLista (request):
    sessdel=request.session.get("data", {"item":[]})
    del request.session["data"]
    return redirect("Mycart")
