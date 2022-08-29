from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import TemplateView

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



#Borrar luego.
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core import mail

def FacturaElectronica(request):
    template_name = "nucleo/FacturaElectronica.html"
    connection = mail.get_connection()
    connection.open()
    correo1 = mail.EmailMessage(
        'Compra en TDE.',
        'Factura de TDE por compra de productos.',
        'proyectoswebutm@gmail.com', #DesdeEmail.
        ['destino@servidor.ext'],    #ParaEmail.
        connection=connection,
    )
    correo1.send() #Para enviar un correo.
    connection.close()

    return render(request, template_name, {'TituloInicio': 'TDE'})
    