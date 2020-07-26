from django.db import models

# Create your models here.
class Cliente(models.Model):
    pnombre = models.CharField(max_length = 50)
    snombre = models.CharField(max_length = 50)
    pape = models.CharField(max_length = 50)
    sape = models.CharField(max_length = 50)
    direccion = models.CharField(max_length= 300)
    celular = models.CharField(max_length = 8)
    activo = models.BooleanField()