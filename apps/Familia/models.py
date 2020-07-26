from django.db import models

# Create your models here.
class Familia(models.Model):
    descripcion = models.CharField(max_length = 50)
    activo = models.BooleanField()