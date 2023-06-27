from django.db import models


# Create your models here.

class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField(default=0)
    origen = models.CharField(max_length=100)
    destacado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre 