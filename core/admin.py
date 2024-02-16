from django.contrib import admin
from core.models import *

# Register your models here.
class ChanceAnimalitosAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'animalito', 'date_sort', 'get_image_path')

admin.site.register(ChanceAnimalitos, ChanceAnimalitosAdmin)

class GranjaPlusAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'animalito', 'date_sort', 'get_image_path')

admin.site.register(GranjaPlus, GranjaPlusAdmin)

class LaGranjitaAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'animalito', 'date_sort', 'get_image_path')

admin.site.register(LaGranjita, LaGranjitaAdmin)

class LaRicachonaAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'animalito', 'date_sort', 'get_image_path')

admin.site.register(LaRicachona, LaRicachonaAdmin)

class LottoActivoAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'animalito', 'date_sort', 'get_image_path')

admin.site.register(LottoActivo, LottoActivoAdmin)

class LottoReyAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'animalito', 'date_sort', 'get_image_path')

admin.site.register(LottoRey, LottoReyAdmin)

# class SelvaPlusAdmin(admin.ModelAdmin):
#     list_display = ('hour_sort', 'animalito', 'date_sort', 'get_image_path')

# admin.site.register(SelvaPlus, SelvaPlusAdmin)

