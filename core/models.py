from django.db import models
from datetime import datetime
from django.conf import settings

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from os.path import join
from .tuples import *

def enviar_mensaje(self):
    datos = {
            'hour_sort': self.hour_sort,
            'animalito': self.animalito,
            'animalito_name': self.get_animalito_display(),  # Obtiene el nombre del animalito
            'date_sort': str(self.date_sort),
            'image_path': self.get_image_path(),
            'modelo': self.__class__.__name__,  # Añade el nombre del modelo
        }
    # Crea un mensaje con los datos que quieres enviar
    message = {
        'type': 'nuevos_datos',
        'data': datos,
    }

    # Obtiene la capa del canal y envía el mensaje
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('grupo_de_datos', message)

# Create your models here.
class ChanceAnimalitos(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/chanceenlinea/{self.animalito}.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        enviar_mensaje(self)

class GranjaPlus(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_GP, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GRANA_PLUS_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/lagranjaplus/{self.animalito}.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        enviar_mensaje(self)

class LaGranjita(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_LG, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GRANJITA_LOTTO_ACTIVO_SELVA_PLUS_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/lagranjita/{self.animalito}.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        enviar_mensaje(self)

class LaRicachona(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_RC, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_LA_RICACHONA_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/laricachona/{self.animalito}.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        enviar_mensaje(self)

class LottoActivo(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_LA, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GRANJITA_LOTTO_ACTIVO_SELVA_PLUS_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/lottoActivo/{self.animalito}.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        enviar_mensaje(self)

class LottoActivoInterRD(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_GP, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GRANJITA_LOTTO_ACTIVO_SELVA_PLUS_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/lottoActivo/{self.animalito}.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        enviar_mensaje(self)

class LottoRey(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_GP, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GRANJITA_LOTTO_ACTIVO_SELVA_PLUS_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/lottorey/{self.animalito}.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        enviar_mensaje(self)

class SelvaPlus(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_SP, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GRANJITA_LOTTO_ACTIVO_SELVA_PLUS_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/selvaplus/{self.animalito}.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        enviar_mensaje(self)

class GuacharoActivo(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_GA, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GUACHARO_ACTIVO_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/guacharoactivo/{self.animalito}.jpg')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        enviar_mensaje(self)

class GranjaMillonaria(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GRANJA_MILLONARIA_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/gm/{self.animalito}.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        enviar_mensaje(self)

class Granjazo(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_GJ, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GRANJAZO_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/gm/{self.animalito}.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        enviar_mensaje(self)