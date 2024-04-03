from django.db import models
from usuarios.models import Propietario

class Categoria(models.Model):
    Id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50,blank=False, null=False)
    esta_activa = models.BooleanField(default=True)    
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_categoria

class Producto(models.Model):
    Id_producto = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(max_length=500, blank=True, null=True)
    precio = models.FloatField(default=0.00)
    existencia = models.FloatField(default=0.00)
    esta_activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)

    def __str__(self):
        return self.producto