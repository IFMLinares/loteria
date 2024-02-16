from django.db import models
from datetime import datetime
from django.conf import settings
from os.path import join
from .tuples import *

# Create your models here.
class ChanceAnimalitos(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/chanceenlinea/{self.animalito}.png')

class GranjaPlus(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_GP, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GRANA_PLUS_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/lagranjaplus/{self.animalito}.png')

class LaGranjita(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_LG, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GRANJITA_LOTTO_ACTIVO_SELVA_PLUS_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/lagranjita/{self.animalito}.png')

class LaRicachona(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_RC, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_LA_RICACHONA_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/laricachona/{self.animalito}.png')

class LottoActivo(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GRANJITA_LOTTO_ACTIVO_SELVA_PLUS_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/lottoActivo/{self.animalito}.png')

class LottoRey(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_GP, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GRANJITA_LOTTO_ACTIVO_SELVA_PLUS_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/lottorey/{self.animalito}.png')
    
class SelvaPlus(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_SP, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GRANJITA_LOTTO_ACTIVO_SELVA_PLUS_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/selvaplus/{self.animalito}.png')