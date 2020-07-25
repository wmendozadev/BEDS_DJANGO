from django.db import models

# Create your models here.

class EstadoVenta(models.Model) :
    estadoVenta= models.CharField(max_length=50)
    activo = models.BooleanField()
    