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

class TripleCalienteAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'a', 'b', 'c', 'zod', 'date_sort')

class TripleCaracasAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'a', 'b', 'c', 'zod', 'date_sort')

class TripleTachiraAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'a', 'b', 'c', 'zod', 'date_sort')

class TrioActivoAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'a', 'b', 'c', 'zod', 'date_sort')

class RicachonaAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'a', 'b', 'c', 'zod', 'date_sort')

class TripleZuliaAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'a', 'b', 'c', 'zod', 'date_sort')

class TripleZamoranoAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'a', 'b', 'c', 'zod', 'date_sort')

class TripleChanceAdmin(admin.ModelAdmin):
    list_display = ('hour_sort', 'a', 'b', 'c', 'zod', 'date_sort')


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

# admin.site.register(TripleCaliente, TripleCalienteAdmin)
# admin.site.register(TripleCaracas, TripleCaracasAdmin)
# admin.site.register(TripleZulia, TripleZuliaAdmin)
# admin.site.register(TripleZamorano, TripleZamoranoAdmin)
# admin.site.register(TripleChance, TripleChanceAdmin)
# admin.site.register(TripleTachira, TripleTachiraAdmin)
# admin.site.register(TrioActivo, TrioActivoAdmin)
# admin.site.register(Ricachona, RicachonaAdmin)


