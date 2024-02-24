#Dashboard es nuestra APP PRINCIPAL

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import FormularioProducto, FormularioPedido # se importa el formulario
from django.contrib.auth.models import User #se importan los usuarios
from .models import Producto, Pedido

# Create your views here
@login_required(login_url='login')
def index(request):
    pedidos = Pedido.objects.all()
    productos = Producto.objects.all()
    contar_usuarios = User.objects.all().count()
    contar_productos = Producto.objects.all().count()
    contar_pedidos = Pedido.objects.all().count()
    if request.method == 'POST':
        form = FormularioPedido(request.POST) 
        if form.is_valid():  # si la validacion fue correcta
            instance = form.save(commit=False)
            instance.usuario = request.user   # asignamos al usuario que esta logueado
            instance.save()
            messages.success(request, "El pedido  se ha creado exitosamente")
            return redirect ('index')
    else:
        form = FormularioPedido()
    context={
        'form': form,
        'pedidos': pedidos,
        'productos': productos,
        'contar_usuarios':contar_usuarios,
        'contar_productos':contar_productos,
        'contar_pedidos':contar_pedidos,
    }
    return render(request, "dashboard/index.html", context)
    

@login_required
def personal(request):
    usuarios = User.objects.all()
    contar_usuarios = usuarios.count()
    context= {
        'usuarios':usuarios,
        'contar_usuarios': contar_usuarios
    }
    return render(request, "dashboard/personal.html", context)

@login_required
def detalles_staff(request, pk):
    usuarios = User.objects.get(id=pk)
    context= {
        'usuarios':usuarios
    } 
    return render(request, "dashboard/detalles_staff.html", context)


@login_required   #Forma más óptima y usada de mostrar
def producto(request):    
    productos = Producto.objects.all()
    contar_usuarios = User.objects.all()
   
    if request.method == 'POST':
        form = FormularioProducto(request.POST) #se crea el formulario
        if form.is_valid():  #si los datos del formulario son validos
            form.save()
            #messages.success(request, "Producto agregado correctamente!") Mensaje con libreria SWAL
            product_name = form.cleaned_data.get('nombre')
            messages.success(request, f"El {product_name} se ha agregado correctamente.")
            
            return redirect('productos')
    else:
        form = FormularioProducto()
    context={'productos':productos,
             'form':form,
             'contar_usuarios':contar_usuarios,
             }

        
    return render(request, "dashboard/producto.html", context)

#Otra forma con SQL menos usado
"""@login_required
def producto(request): 
    productos = Producto.objects.raw("SELECT * FROM dashboard_Producto" )
    context={'productos':productos}
    return render(request, "dashboard/producto.html", context)"""


@login_required
def pedido(request):
    pedidos = Pedido.objects.all()
    context = {
        "pedidos":pedidos
        }
    return render(request, "dashboard/pedido.html", context)


def eliminar_producto(request, pk): #pk=sinonimo de parámetro
    producto = Producto.objects.get(id = pk)
    if request.method == "POST":
        producto.delete()
        messages.success(request, "Producto eliminado correctamente!")
        return redirect('productos')
    return render(request, "dashboard/eliminar_producto.html")

def actualizar_producto(request, pk):
    producto = Producto.objects.get(id = pk)
    if request.method == 'POST':
        form = FormularioProducto(request.POST, instance=producto) #Se pasa la instancia para que se edite lo que ya existe en
        if form.is_valid():  #si los datos del formulario son validos
            form.save()
            messages.success(request, "Producto actualizado correctamente!")
            return redirect('productos')
    else:
        form = FormularioProducto(instance=producto)
        
        
    context = {
        'form': form,
    }
    
    return render(request, "dashboard/actualizar_producto.html", context)

