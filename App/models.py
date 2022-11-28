from django.db import models

# Create your models here.
class Docente(models.Model):
  nombre = models.CharField(max_length=15)
  apellido = models.CharField(max_length=15)
  fono = models.CharField(max_length=15)
  nivelAcademico = models.CharField(max_length=50)
  cursosAsignados = models.IntegerField()
  especialidad = models.CharField(max_length=50)
