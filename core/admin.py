from django.contrib import admin
from core.models import *

# Register your models here.
class ChanceAnimalitosAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'animalito', 'date_sort', 'get_image_path')

class GranjaPlusAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'animalito', 'date_sort', 'get_image_path')

class LaGranjitaAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'animalito', 'date_sort', 'get_image_path')

class LaRicachonaAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'animalito', 'date_sort', 'get_image_path')

class LottoActivoAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'animalito', 'date_sort', 'get_image_path')

class LottoReyAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'animalito', 'date_sort', 'get_image_path')

class SelvaPlusAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'animalito', 'date_sort', 'get_image_path')

class GuacharoActivoAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'animalito', 'date_sort', 'get_image_path')

class LottoActivoInterRDAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'animalito', 'date_sort', 'get_image_path')

class GranjaMillonariaAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'animalito', 'date_sort', 'get_image_path')

class GranjazoAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'animalito', 'date_sort', 'get_image_path')


admin.site.register(ChanceAnimalitos, ChanceAnimalitosAdmin)
admin.site.register(GranjaPlus, GranjaPlusAdmin)
admin.site.register(LaGranjita, LaGranjitaAdmin)
admin.site.register(LaRicachona, LaRicachonaAdmin)
admin.site.register(LottoActivo, LottoActivoAdmin)
admin.site.register(LottoRey, LottoReyAdmin)
admin.site.register(SelvaPlus, SelvaPlusAdmin)
admin.site.register(GuacharoActivo, GuacharoActivoAdmin)
admin.site.register(LottoActivoInterRD, LottoActivoInterRDAdmin)
admin.site.register(GranjaMillonaria, GranjaMillonariaAdmin)
admin.site.register(Granjazo, GranjazoAdmin)

