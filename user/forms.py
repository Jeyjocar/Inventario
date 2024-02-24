from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm
from dashboard.models import Producto
from . models import Perfil

#Formulario para crear el usuario
class  CreateUserForm(UserCreationForm):
    nombre= forms.CharField()   
    apellido = forms.CharField()
    email= forms.EmailField()

    class Meta:
        model = User
        fields= ['nombre', 'apellido', 'email', 'username','password1','password2']

#Formulario para actualizar el usuario
class UsuarioUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields =['username', 'email']

#Formulario para actualizar el perfil del usuario Jeyfrey Calero
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Perfil
        fields =['nombre', 'apellido', 'telefono', 'direccion', 'imagen']
        

