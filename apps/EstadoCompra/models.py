from django.db import models

# Create your models here.

class EstadoCompra(models.Model):
    estadoCompra = models.CharField(max_length = 50)
    activo = models.BooleanField()