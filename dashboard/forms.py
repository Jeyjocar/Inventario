#Creamos el FORM para a agregar

from django import forms
from user.models import Perfil
from . models import Producto, Pedido 



class FormularioProducto(forms.ModelForm):
    
    class Meta:
        model = Producto  # Establecemos la clase de modelo al que nos referimos
        fields = ['nombre', 'categoria','cantidad', 'precio']
    
#Formulario para crear el pedido
class FormularioPedido(forms.ModelForm):
    
    class Meta:
        model = Pedido
        fields =['producto', 'cantidad_pedida', 'precio']  
        

class Perfil(forms.ModelForm):
    
    class Meta:
        model = Perfil
        fields =['nombre', 'apellido', 'telefono', 'direccion', 'imagen']