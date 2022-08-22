from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView

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

class VistaPaginaInicio(TemplateView):
    template_name = "nucleo/Inicio.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'TituloInicio': 'TDE'})

# La vista de la tienda que estaba aquí en la vista de la app nucleo, fue movida
# a la vista de la app tienda. 

class VistaPaginaAcerca(TemplateView):
    template_name = "nucleo/Acerca.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'TituloInicio': 'TDE'})


class VistaPaginaContacto(TemplateView):
    template_name = "nucleo/Contacto.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'TituloInicio': 'TDE'})


class VistaPaginaFormaPago(TemplateView):
    template_name = "nucleo/FormaPago.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'TituloInicio': 'TDE'})
