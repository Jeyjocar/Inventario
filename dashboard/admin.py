from django.contrib import admin

from .models import *
from django.contrib.auth.models import Group

# Register your models here.
admin.site.site_header = "Inventario Jeyfrey Calero" 

class ProductoAdmin(admin.ModelAdmin):
    list_display= ('nombre', 'cantidad','categoria')
    list_filter = ['categoria']

class PedidoAdmin(admin.ModelAdmin):
    list_display=("producto","usuario","precio")
    list_filter = ['fecha']



admin.site.register(Producto,ProductoAdmin)

admin.site.register(Pedido,PedidoAdmin)


