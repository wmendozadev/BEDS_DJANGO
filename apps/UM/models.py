from django.db import models

# Create your models here.
class UM(models.Model):
    descripcion = models.CharField(max_length = 50)
    activo = models.BooleanField()