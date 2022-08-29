from django.contrib import admin
from .models import Categoria
from .models import Producto

# Register your models here.
class CategoriaAdministrador(admin.ModelAdmin):
    readonly_fields = ('idnumcat', 'creado', 'modificado')

class ProductoAdministrador(admin.ModelAdmin):
    readonly_fields = ('idnumprod', 'agregadop', 'modificadop')
    
    

admin.site.register(Categoria, CategoriaAdministrador)
admin.site.register(Producto, ProductoAdministrador)
