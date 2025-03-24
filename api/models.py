from django.db import models

# Create your models here.

class Cita(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, verbose_name='Nombres')
    apellido = models.CharField(max_length=150, verbose_name='Apellidos')
    documento = models.IntegerField(verbose_name='N° de documento')
    fecha = models.DateField(verbose_name='Fecha')
    hora = models.CharField(max_length=10, verbose_name='Horas')
    servicio = models.CharField(max_length=100, verbose_name="Servicio", null=True)