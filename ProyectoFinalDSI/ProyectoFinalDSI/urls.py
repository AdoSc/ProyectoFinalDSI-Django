"""ProyectoFinalDSI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from nucleo.views import VistaPaginaInicio, VistaPaginaAcerca, VistaPaginaContacto, VistaPaginaFormaPago
from tienda.views import VistaListaCategoria, VistaListaProducto, FiltrarProductos, Cart , Detalle,Mycart, Comprar, BorrarLista


from django.conf import settings



urlpatterns = [
    path('', VistaPaginaInicio.as_view(), name="Inicio"),
    path('Categoria/', VistaListaCategoria.as_view(), name="Categoria"),
    path('Producto/', VistaListaProducto.as_view(), name="Producto"),   
    path('FiltrarProductos/<slug>', FiltrarProductos, name="FiltrarProductos"),
    #borre la ruta comprar
    path('FormaPago/', VistaPaginaFormaPago.as_view(), name="FormaPago"),   #Restaurada.

    path('Acerca/', VistaPaginaAcerca.as_view(), name="Acerca"),
    path('Contacto/', VistaPaginaContacto.as_view(), name="Contacto"),
   #--------------------nuevas rutas---------------

    path('cart/<slug>', Cart , name="cart"),
    path('detalles/<slug>', Detalle , name="detail"),
    path('mycart/', Mycart , name="Mycart"),
    path('comprar/', Comprar , name="Comprar"),

    #Re-definido oara borrar lista de compras.
    path('BorrarLista/', BorrarLista, name="BorrarLista"),


    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

