from django.db import models
from datetime import datetime

# Create your models here.

class Sorteo(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre del Sorteo')

    def __str__(self):
        return  self.name

class Animal(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre del Animal')
    number = models.PositiveIntegerField(verbose_name="Número de animalito")

    def __str__(self):
        return  self.name

class Resultado_Animalito(models.Model):
    sorteo = models.ForeignKey(Sorteo, on_delete=models.PROTECT, verbose_name="Sorteo")
    animal = models.ManyToManyField(Animal)
    hour_sort = models.TimeField(verbose_name="Hora del sorteo", null=True)
    date_result_add = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.sorteo)