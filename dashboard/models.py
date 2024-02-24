from django.db import models

from django.contrib.auth.models import User

# Create your models here.
CATEGORIA = [
    ("Electrónicos", "Electrónicos"),
    ("Muebles","Muebles"),
    ("Electrodomésticos", "Electrodomésticos"),
    ("Limpieza", "Limpieza"),
    ("Comestibles", "Comestibles"),
]

class Producto(models.Model):
    nombre= models.CharField(max_length=100)
    categoria= models.CharField(max_length=100, choices=CATEGORIA, null= True)
    cantidad=models.PositiveIntegerField(null=True)
    precio= models.PositiveIntegerField(null=True)


    def __str__(self):
        return f'{self.nombre}'

class Pedido(models.Model):
    producto= models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    usuario= models.ForeignKey(User, models.CASCADE, null=True)
    cantidad_pedida= models.PositiveIntegerField(null=True)
    precio=models.PositiveIntegerField(null=True)
    fecha=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.producto} ordenado por {self.usuario}' 



 
