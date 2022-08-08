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
#from nucleo import views as vista_nucleo
#from tienda import views as vista_tienda
from nucleo.views import VistaPaginaInicio, VistaPaginaAcerca, VistaPaginaContacto, VistaPaginaCompra
from tienda.views import VistaListaCategoria, VistaListaProducto, FiltrarProductos
#from tienda.views import VistaDetalleProducto

from django.conf import settings

urlpatterns = [
    path('', VistaPaginaInicio.as_view(), name="Inicio"),
    path('Categoria/', VistaListaCategoria.as_view(), name="Categoria"),
    path('Producto/', VistaListaProducto.as_view(), name="Producto"),    #Nueva dirección.
    path('FiltrarProductos/<slug>', FiltrarProductos, name="FiltrarProductos"),
    #path('Producto/<int:pk>/<slug:slug>/', VistaDetalleProducto.as_view(), name="Producto"),    #Nueva dirección.
    path('Acerca/', VistaPaginaAcerca.as_view(), name="Acerca"),
    path('Contacto/', VistaPaginaContacto.as_view(), name="Contacto"),
    path('Comprar/', VistaPaginaCompra.as_view(), name="Comprar"),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

