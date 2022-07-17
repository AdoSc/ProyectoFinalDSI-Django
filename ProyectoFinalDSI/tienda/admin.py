from django.contrib import admin
from .models import Catalogo
from .models import Producto

# Register your models here.
class CatalogoAdministrador(admin.ModelAdmin):
    readonly_fields = ('enlace', 'creado', 'modificado')

class ProductoAdministrador(admin.ModelAdmin):
    readonly_fields = ('agregadop', 'modificadop')
    
    

admin.site.register(Catalogo, CatalogoAdministrador)
admin.site.register(Producto, ProductoAdministrador)
