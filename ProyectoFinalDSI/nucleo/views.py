from django.shortcuts import render, HttpResponse

html_base="""
    <h1>Tienda de dispositivos electrónicos.</h1>
    <ul>
        <li><a href="/">Inicio</a></li>
        <li><a href="/Tienda/">Tienda</a></li>
        <li><a href="/Producto/">Producto</a></li>
        <li><a href="/Acerca/">Acerca</a></li>
        <li><a href="/Contacto/">Contacto</a></li>
    </ul>
"""

# Create your views here.
def Inicio(request):
    return render(request, "nucleo/Inicio.html") # Envía la dirección del código.

# La vista de la tienda que estaba aquí en la vista de la app nucleo, fue movida
# a la vista de la app tienda. 

def Acerca(request):
    return render(request, "nucleo/Acerca.html") # Envía la dirección del código.

def Contacto(request):
    return render(request, "nucleo/Contacto.html") # Envía la dirección del código.
