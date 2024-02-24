from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    nombre =models.CharField(max_length = 200, null = True)
    apellido =models.CharField(max_length = 200, null = True)
    staff = models.OneToOneField(User, on_delete = models.CASCADE, null = True)
    direccion = models.CharField(max_length = 200, null = True)
    telefono = models.CharField(max_length = 20, null = True)
    imagen = models.ImageField(default = "Avatar", upload_to = "Profile_Image")
    def __str__(self):
        return f"Perfil {self.staff.username}"

# Create your models here.
