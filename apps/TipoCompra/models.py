from django.db import models

# Create your models here.
class TipoCompra(models.Model):
    tipoCompra = models.CharField(max_length = 50)
    activo = models.BooleanField()