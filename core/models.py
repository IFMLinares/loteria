from django.db import models
from datetime import datetime, timedelta

from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.db import models
import re

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from os.path import join
from .tuples import *
import os
from django.utils import timezone

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

def enviar_mensaje_loterias(self):
    datos = {
            'hour_sort': self.hour_sort,
            'date_sort': self.date_sort.isoformat(),  # Convertimos el objeto date a una cadena de texto
            'a': self.a,
            'b': self.b,
            'c': self.c,
            'zod': self.zod,
            'modelo': self.__class__.__name__,
        }
    message = {
        'type': 'nuevos_datos',
        'data': datos,
    }
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('grupo_de_datos', message)

def enviar_mensaje_loterias_tz(self):
    datos = {
            'hour_sort': self.hour_sort,
            'date_sort': self.date_sort.isoformat(),  # Convertimos el objeto date a una cadena de texto
            'a': self.a,
            'c': self.c,
            'zod': self.zod,
            'modelo': self.__class__.__name__,
        }
    message = {
        'type': 'nuevos_datos',
        'data': datos,
    }

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('grupo_de_datos', message)

def enviar_mensaje_loterias_esp(self):
    datos = {
            'hour_sort': self.hour_sort,
            'date_sort': self.date_sort.isoformat(),  # Convertimos el objeto date a una cadena de texto
            'a': self.a,
            'modelo': self.__class__.__name__,
        }
    message = {
        'type': 'nuevos_datos',
        'data': datos,
    }

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('grupo_de_datos', message)

def validate_numeric(value):
    if not re.match('^[0-9]*$', value):
        raise ValidationError('El valor debe ser numérico')
# Create your models here.

# class LoggedInUser(models.Model):
#     user = models.OneToOneField(User, related_name='logged_in_user', on_delete=models.CASCADE, null=True, blank=True)
#     session_key = models.CharField(max_length=32, null=True, blank=True)

# def create_logged_in_user(sender, instance, created, **kwargs):
#     if created:
#         LoggedInUser.objects.create(user=instance)

# models.signals.post_save.connect(create_logged_in_user, sender=User)

# videos
from django.db import models
import os

class VideoModel(models.Model):
    name = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/')
    fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def was_uploaded_today(self):
        return self.fecha_creacion.date() == timezone.localtime(timezone.now()).date()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original
        # Llama a la función para enviar el mensaje
        enviar_mensaje(self)

class VideoModelToday(models.Model):
    video = models.FileField(upload_to='videos/')
    fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def was_uploaded_today(self):
        return self.fecha_creacion.date() == timezone.localtime(timezone.now()).date()
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

class TimeView(models.Model):
    time_in_milliseconds = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f"Tiempo de visualización actual: {self.time_in_milliseconds} ms"
# modelos de los animalitos 

class ChanceAnimalitos(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'Chance Animalitos'
        verbose_name_plural = 'Chance Animalitos'

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/chanceenlinea/{self.animalito}.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        enviar_mensaje(self)
    
    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

class GranjaPlus(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_GP, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GRANA_PLUS_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'Granja Plus'
        verbose_name_plural = 'Granja Plus'

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/lagranjaplus/{self.animalito}.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        enviar_mensaje(self)
        
    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

class LaGranjita(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_LG, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GRANJITA_LOTTO_ACTIVO_SELVA_PLUS_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'La Granjita'
        verbose_name_plural = 'La Granjita'

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/lagranjita/{self.animalito}.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        
        enviar_mensaje(self)
        
    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

class LaRicachona(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_RC, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_LA_RICACHONA_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'La Ricachona Animalitos'
        verbose_name_plural = 'La Ricachona Animalitos'

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/laricachona/{self.animalito}.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        
        enviar_mensaje(self)
        
    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

class LottoActivo(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GRANJITA_LOTTO_ACTIVO_SELVA_PLUS_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'Lotto Activo'
        verbose_name_plural = 'Lotto Activo'

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/lottoActivo/{self.animalito}.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        
        enviar_mensaje(self)
        
    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

class LottoActivoInterRD(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_GP, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GRANJITA_LOTTO_ACTIVO_SELVA_PLUS_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'lotto Activo Inter RD'
        verbose_name_plural = 'Lotto Activo Inter RD'

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/lottoActivo/{self.animalito}.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        
        enviar_mensaje(self)
        
    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

class LottoRey(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_GP, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GRANJITA_LOTTO_ACTIVO_SELVA_PLUS_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'Lotto Rey'
        verbose_name_plural = 'Lotto Rey'

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/lottorey/{self.animalito}.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        
        enviar_mensaje(self)
        
    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

class SelvaPlus(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_SP, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GRANJITA_LOTTO_ACTIVO_SELVA_PLUS_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'Selva Plus'
        verbose_name_plural = 'Selva Plus'

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/selvaplus/{self.animalito}.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        
        enviar_mensaje(self)
        
    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

class GuacharoActivo(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_SP, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GUACHARO_ACTIVO_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'Guacharo Activo'
        verbose_name_plural = 'Guacharo Activo'

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/guacharoactivo/{self.animalito}.jpg')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        
        enviar_mensaje(self)
        
    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

class GranjaMillonaria(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_GM, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GRANJA_MILLONARIA_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'Ganja Millonaria'
        verbose_name_plural = 'Granja Millonaria'

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/gm/{self.animalito}.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        
        enviar_mensaje(self)
        
    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

class Granjazo(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_GJO, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=2, choices=ANIMALITO_GRANJAZO_CHOICES, verbose_name="Animalito")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'Granjazo'
        verbose_name_plural = 'Granjazo'

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/gm/{self.animalito}.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        
        enviar_mensaje(self)
        
    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

class Terminalito(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_TO, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=3, choices=NUMERO_CHOICES, verbose_name="Nro ")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'Terminalito'
        verbose_name_plural = 'Terminalito'

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/terminalito/r{self.animalito}.jpg')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        
        enviar_mensaje(self)
        
    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

class FruitaGana(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=3, choices=FRUITA_CHOICES, verbose_name="Nro ")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'Fruita Gana'
        verbose_name_plural = 'Fruita Gana'

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/fruita_gana/{self.animalito}.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        
        enviar_mensaje(self)
        
    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

class Guacharito(models.Model):
    hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_GP, verbose_name="Hora del sorteo")
    animalito = models.CharField(max_length=3, choices=GUACHARITO_CHOICES, verbose_name="Nro ")
    date_sort = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'Guacharito'
        verbose_name_plural = 'Guacharito'

    def get_image_path(self):
        return join(settings.STATIC_URL, f'img/guacharito/{self.animalito}.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        
        enviar_mensaje(self)
        
    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

# Modelo de las Loterias

class TripleCaliente(models.Model):
    hour_sort = models.CharField(max_length=9, choices=LOTERY_CHOICES_TC, verbose_name="Hora del sorteo")
    date_sort = models.DateField(auto_now=True)
    a = models.CharField(max_length=20, validators=[validate_numeric])
    b = models.CharField(max_length=20, validators=[validate_numeric])
    c = models.CharField(max_length=20, validators=[validate_numeric])
    zod = models.CharField(max_length=9, choices=ZOD_CHOICES)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'Loteria Triple Caliente'
        verbose_name_plural = 'Loteria Triple Caliente'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        enviar_mensaje_loterias(self)
        
    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

class TripleCaracas(models.Model):
    hour_sort = models.CharField(max_length=9, choices=LOTERY_CHOICES_TCCS_TCH, verbose_name="Hora del sorteo")
    date_sort = models.DateField(auto_now=True)
    a = models.CharField(max_length=20, validators=[validate_numeric])
    b = models.CharField(max_length=20, validators=[validate_numeric])
    c = models.CharField(max_length=20, validators=[validate_numeric])
    zod = models.CharField(max_length=9, choices=ZOD_CHOICES)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'Loteria Triple Caracas'
        verbose_name_plural = 'Loteria Triple Caracas'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        enviar_mensaje_loterias(self)
        
    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

class TripleZulia(models.Model):
    hour_sort = models.CharField(max_length=9, choices=LOTERY_CHOICES_ZL, verbose_name="Hora del sorteo")
    date_sort = models.DateField(auto_now=True)
    a = models.CharField(max_length=20, validators=[validate_numeric])
    b = models.CharField(max_length=20, validators=[validate_numeric])
    c = models.CharField(max_length=20, validators=[validate_numeric])
    zod = models.CharField(max_length=9, choices=ZOD_CHOICES)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'Loteria Triple Zulia'
        verbose_name_plural = 'Loteria Triple Zulia'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        enviar_mensaje_loterias(self)
        
    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

class TripleZamorano(models.Model):
    hour_sort = models.CharField(max_length=9, choices=LOTERY_CHOICES_ZA, verbose_name="Hora del sorteo")
    date_sort = models.DateField(auto_now=True)
    a = models.CharField(max_length=20, validators=[validate_numeric])
    # b = models.CharField(max_length=20, validators=[validate_numeric])
    c = models.CharField(max_length=20, validators=[validate_numeric])
    zod = models.CharField(max_length=9, choices=ZOD_CHOICES)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'Loteria Triple Zamorano'
        verbose_name_plural = 'Loteria Triple Zamorano'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        enviar_mensaje_loterias_tz(self)
        
    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

class TripleChance(models.Model):
    hour_sort = models.CharField(max_length=9, choices=LOTERY_CHOICES_TCCS_TCH, verbose_name="Hora del sorteo")
    date_sort = models.DateField(auto_now=True)
    a = models.CharField(max_length=20, validators=[validate_numeric])
    b = models.CharField(max_length=20, validators=[validate_numeric])
    c = models.CharField(max_length=20, validators=[validate_numeric])
    zod = models.CharField(max_length=9, choices=ZOD_CHOICES)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'Loteria Triple Chance'
        verbose_name_plural = 'Loteria Triple Chance'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        enviar_mensaje_loterias(self)
        
    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

class TripleTachira(models.Model):
    hour_sort = models.CharField(max_length=9, choices=LOTERY_CHOICES_TAC, verbose_name="Hora del sorteo")
    date_sort = models.DateField(auto_now=True)
    a = models.CharField(max_length=20, validators=[validate_numeric])
    b = models.CharField(max_length=20, validators=[validate_numeric])
    c = models.CharField(max_length=20, validators=[validate_numeric])
    zod = models.CharField(max_length=9, choices=ZOD_CHOICES)

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'Loteria Triple Tachira'
        verbose_name_plural = 'Loteria Triple Tachira'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        enviar_mensaje_loterias(self)
    # Otros campos...

    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

class TrioActivo(models.Model):
    hour_sort = models.CharField(max_length=9, choices=LOTERY_CHOICES_TA, verbose_name="Hora del sorteo")
    date_sort = models.DateField(auto_now=True)
    a = models.CharField(max_length=20, validators=[validate_numeric])
    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'Loteria Trio Activo'
        verbose_name_plural = 'Loteria Trio Activo'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        enviar_mensaje_loterias_esp(self)
        
    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

class Ricachona(models.Model):
    hour_sort = models.CharField(max_length=9, choices=LOTERY_CHOICES_RC, verbose_name="Hora del sorteo")
    date_sort = models.DateField(auto_now=True)
    a = models.CharField(max_length=20, validators=[validate_numeric])

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'Loteria Ricachona'
        verbose_name_plural = 'Loteria Ricachona'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        enviar_mensaje_loterias_esp(self)
        
    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

class Ricachona(models.Model):
    hour_sort = models.CharField(max_length=9, choices=LOTERY_CHOICES_RC, verbose_name="Hora del sorteo")
    date_sort = models.DateField(auto_now=True)
    a = models.CharField(max_length=20, validators=[validate_numeric])

    class Meta:
        unique_together = ('hour_sort', 'date_sort',)
        verbose_name = 'Loteria Ricachona'
        verbose_name_plural = 'Loteria Ricachona'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Llama al método save original

        # Llama a la función para enviar el mensaje
        enviar_mensaje_loterias_esp(self)
        
    @classmethod
    def eliminar_registros_antiguos(cls):
        fecha_limite = timezone.now().date() - timedelta(days=2)
        cls.objects.filter(date_sort__lt=fecha_limite).delete()

# Modelo de Triple zamorano 
# utiliza HOUR_CHOICES_10_12_2_4 
# tiene los campos hour_sort, date_sort, a, c, zod

# class TripleZamorano(models.Model):
#     hour_sort = models.CharField(max_length=9, choices=HOUR_CHOICES_10_12_2_4, verbose_name="Hora del sorteo")
#     date_sort = models.DateField(auto_now=True)
#     a = models.CharField(max_length=20, validators=[validate_numeric])
#     c = models.CharField(max_length=20, validators=[validate_numeric])
#     zod = models.CharField(max_length=9, choices=ZOD_CHOICES)

#     class Meta:
#         unique_together = ('hour_sort', 'date_sort',)
#         verbose_name = 'Loteria Triple Zamorano 10-12-2-4'
#         verbose_name_plural = 'Loteria Triple Zamorano 10-12-2-4'

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)  # Llama al método save original

#         # Llama a la función para enviar el mensaje
#         enviar_mensaje_loterias_tz(self)
        
#     @classmethod
#     def eliminar_registros_antiguos(cls):
#         fecha_limite = timezone.now().date() - timedelta(days=2)
#         cls.objects.filter(date_sort__lt=fecha_limite).delete()

