from django.db import models

# Create your models here.
class PerfilProfesional(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    carrera = models.CharField(max_length=100)
    celular = models.CharField(max_length=15)

    def _str_(self):
        return f"{self.nombres} {self.apellidos}"