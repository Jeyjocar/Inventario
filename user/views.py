from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.forms import UserCreationForm
from dashboard.models import Producto
from .forms import CreateUserForm, UsuarioUpdateForm, ProfileUpdateForm
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == 'POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            #messages.success(request, "Usuario registrado correctamente")
            new_register = form.cleaned_data.get('username') #libreria interna de Django para mensajes
            messages.success(request, f"El usuario {new_register} ha sido registrado exitosamente!")
            return redirect('login')
    else:
        form= CreateUserForm()

    context={
        'form':form
    }
    return render(request, 'user/register.html',context)
 
                                
def perfil(request):
    return render(request, 'user/perfil.html')


def actualizar_Perfil(request):
    if request.method=='POST':
        user_form = UsuarioUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.perfil)
    
    # Verificar si los dos formularios son validos
        if user_form.is_valid() and profile_form.is_valid():
            # Guardar la informacion en el modelo de usuario y su respectivo perfil
            user_form.save()
            profile_form.save()
            #messages.success(request,"Perfil actualizado correctamente!")
            update_perfil = user_form.cleaned_data.get('username') #libreria interna de Django para mensajes
            messages.success(request, f"El usuario {update_perfil} ha sido actualizado exitosamente!")
            return redirect('perfil')
    else:
        user_form = UsuarioUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.perfil)
        context = {
            "usuario": user_form,
            "perfil" :profile_form 
        }
    return render(request, 'user/actualizar_Perfil.html', context)  

