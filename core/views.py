import json
from datetime import time, date, timedelta
from collections import defaultdict
from django.apps import apps
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, ListView, CreateView
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from .models import *
from django.conf import settings
# Create your views here.

def ContextData(day):
    context = {}
    models = [ 
        ChanceAnimalitos,
        GranjaPlus,
        LaGranjita,
        LaRicachona,
        LottoActivo,
        LottoRey,
        SelvaPlus,
        GuacharoActivo,
        LottoActivoInterRD,
        GranjaMillonaria,
        Granjazo,
        Terminalito,
        Guacharito,
        TripleCaliente,
        TripleCaracas,
        TripleZamorano,
        TripleZulia,
        TripleChance,
        TripleTachira,
        TrioActivo,
        Ricachona,
    ]

    for model in models:
        model_name = model.__name__
        hours = [choice[0] for choice in model._meta.get_field('hour_sort').choices]
        records = model.objects.filter(date_sort=day)
        records_dict = {record.hour_sort: record for record in records}

        context[model_name] = []
        for hour in hours:
            if hour in records_dict:
                record = records_dict[hour]
                if model_name in ['TrioActivo', 'Ricachona']:
                    # Maneja los nuevos modelos aquí
                    context[model_name].append({
                        'hour_sort': record.hour_sort,
                        'a': record.a,
                    })
                elif model_name in ['TripleCaliente', 'TripleCaracas', 'TripleZulia', 'TripleChance', 'TripleTachira']:
                    context[model_name].append({
                        'hour_sort': record.hour_sort,
                        'a': record.a,
                        'b': record.b,
                        'c': record.c,
                        'zod': record.zod,
                    })
                elif model_name in ['TripleZamorano']:
                        context[model_name].append({
                            'hour_sort': record.hour_sort,
                            'a': record.a,
                            'c': record.c,
                            'zod': record.zod,
                        })
                else:
                    context[model_name].append({
                        'hour_sort': record.hour_sort,
                        'animalito': record.animalito,
                        'animalito_name': dict(model._meta.get_field('animalito').choices)[record.animalito],
                        'image_path': record.get_image_path(),
                    })
            else:
                if model_name in ['TrioActivo', 'Ricachona']:
                    context[model_name].append({
                        'hour_sort': hour,
                        'a': '---',
                    })
                elif model_name in ['TripleZamorano']:
                        context[model_name].append({
                            'hour_sort': hour,
                            'a': '---',
                            'c': '---',
                            'zod': '---',
                        })
                elif model_name in ['TripleCaliente', 'TripleCaracas', 'TripleZulia', 'TripleChance', 'TripleTachira']:
                    context[model_name].append({
                        'hour_sort': hour,
                        'a': '---',
                        'b': '---',
                        'c': '---',
                        'zod': '---',
                    })
                else:
                    context[model_name].append({
                        'hour_sort': hour,
                        'animalito': '---',
                        'animalito_name': '---',
                        'image_path': '----------',
                    })
    return context

def ContextData_vid(day):
    context = {}
    models = [ 
        GuacharoActivo,
        LottoActivo,
        LaGranjita,
        SelvaPlus,
    ]

    for model in models:
        model_name = model.__name__
        hours = [choice[0] for choice in model._meta.get_field('hour_sort').choices]
        records = model.objects.filter(date_sort=day)
        records_dict = {record.hour_sort: record for record in records}

        context[model_name] = []
        for hour in hours:
            if hour in records_dict:
                record = records_dict[hour]
                hour_numeric = int(hour[:2])  # Extraemos las dos primeras cifras como número
                group_animal = 1 if 8 <= hour_numeric <= 12 else 2
                context[model_name].append({
                    'hour_sort': record.hour_sort,
                    'animalito': record.animalito,
                    'animalito_name': dict(model._meta.get_field('animalito').choices)[record.animalito],
                    'image_path': record.get_image_path(),
                    'group_animal': group_animal,
                })
            else:
                hour_numeric = int(hour[:2])  # Extraemos las dos primeras cifras como número
                group_animal = 1 if 8 <= hour_numeric <= 12 else 2
                context[model_name].append({
                    'hour_sort': hour,
                    'animalito': '---',
                    'animalito_name': '---',
                    'image_path': '----------',
                    'group_animal': group_animal,
                })
    return context

class LotteryView(View):
    def get(self, request):
        context = ContextData(date.today())
        context['yesterday'] = ContextData(date.today() - timedelta(days=1))
        
        # Try to get the video with the name "video_1" from the database
        try:
            video = VideoModel.objects.get(name='video_1')
        except VideoModel.DoesNotExist:
            video = None
        
        # Try to get the video with the name "video_1" from the database
        try:
            video_2 = VideoModel.objects.get(name='video_2')
        except VideoModel.DoesNotExist:
            video_2 = None

        # Try to get the video with the name "video_1" from the database
        try:
            video_3 = VideoModel.objects.get(name='video_3')
        except VideoModel.DoesNotExist:
            video_3 = None

        # Try to get the video with the name "video_1" from the database
        try:
            video_4 = VideoModel.objects.get(name='video_4')
        except VideoModel.DoesNotExist:
            video_4 = None
        
        # Try to get the video with the name "video_1" from the database
        try:
            video_5 = VideoModel.objects.get(name='video_5')
        except VideoModel.DoesNotExist:
            video_5 = None

        # Add the video to the context
        time_view = TimeView.objects.first()
        context['time'] = time_view.time_in_milliseconds
        context['video'] = video
        context['video_2'] = video_2
        context['video_3'] = video_3
        context['video_4'] = video_4
        context['video_5'] = video_5

        return render(request, 'lotoview/index.html', context)


class VideosDelDiaListView(ListView):
    model = VideoModelToday
    template_name = 'lotoview/today_vid.html'  # Nombre de tu template
    context_object_name = 'videos'

    def get_queryset(self):
        # Filtramos los videos que tienen la fecha de creación igual a hoy
        hoy = timezone.localtime(timezone.now()).date()
        return VideoModelToday.objects.filter(fecha_creacion__date=hoy)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['animalitos'] = ContextData_vid(date.today())
        return context

# L I S T A D O S   D E   A N I M A L I T O S
@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(staff_member_required, name='dispatch')
class IndexView(View):
    def get(self, request):
        context = {}
        context['title'] = "Inicio"
        context['entity'] = 'Pagina de inicio'
        
        # Try to get the video with the name "video_1" from the database
        try:
            video = VideoModel.objects.get(name='video_1')
        except VideoModel.DoesNotExist:
            video = None
        
        # Try to get the video with the name "video_1" from the database
        try:
            video_2 = VideoModel.objects.get(name='video_2')
        except VideoModel.DoesNotExist:
            video_2 = None

        # Try to get the video with the name "video_1" from the database
        try:
            video_3 = VideoModel.objects.get(name='video_3')
        except VideoModel.DoesNotExist:
            video_3 = None

        # Try to get the video with the name "video_1" from the database
        try:
            video_4 = VideoModel.objects.get(name='video_4')
        except VideoModel.DoesNotExist:
            video_4 = None
        # Try to get the video with the name "video_1" from the database
        try:
            video_5 = VideoModel.objects.get(name='video_5')
        except VideoModel.DoesNotExist:
            video_5 = None


        # Add the video to the context
        time_view = TimeView.objects.first()
        time_in_seconds = time_view.time_in_milliseconds // 1000
        context['time'] = time_in_seconds
        context['video'] = video
        context['video_2'] = video_2
        context['video_3'] = video_3
        context['video_4'] = video_4
        context['video_5'] = video_5
        # Añadir Guacharito al contexto
        guacharito_records = Guacharito.objects.filter(date_sort=timezone.localtime(timezone.now()).date())
        context['Guacharito'] = guacharito_records

        return render(request, 'admin/erp/index/index.html', context)
    
    def post(self, request):
        message = {
            'type': 'nuevos_datos',
            'data': 'reload',
        }
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)('grupo_de_datos', message)

@method_decorator(staff_member_required, name='dispatch')
class AdminChanceAnimalitos(ListView):
    model = ChanceAnimalitos
    template_name = "admin/erp/animalitos/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Animalitos"
        context['entity'] = 'ChanceAnimalitos'
        context['create_url'] = reverse_lazy('core:chance_animalitos_add')
        context['url'] = reverse_lazy('core:chanceAnimalitos')
        context['model_name'] = self.model.__name__
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminGranjaPlus(ListView):
    model = GranjaPlus
    template_name = "admin/erp/animalitos/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Animalitos"
        context['entity'] = 'GranjaPlus'
        context['create_url'] = reverse_lazy('core:granja_plus_add')
        context['url'] = reverse_lazy('core:granjaPlus')
        context['model_name'] = self.model.__name__
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminLaGranjita(ListView):
    model = LaGranjita
    template_name = "admin/erp/animalitos/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Animalitos"
        context['entity'] = 'LaGranjita'
        context['create_url'] = reverse_lazy('core:la_granjita_add')
        context['url'] = reverse_lazy('core:laGranjita')
        context['model_name'] = self.model.__name__
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminLaRicachona(ListView):
    model = LaRicachona
    template_name = "admin/erp/animalitos/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Animalitos"
        context['entity'] = 'LaRicachona'
        context['url'] = reverse_lazy('core:laRicachona')
        context['create_url'] = reverse_lazy('core:ricachona_add')
        context['model_name'] = self.model.__name__
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminLottoActivo(ListView):
    model = LottoActivo
    template_name = "admin/erp/animalitos/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Animalitos"
        context['entity'] = 'LottoActivo'
        context['url'] = reverse_lazy('core:lottoActivo')
        context['create_url'] = reverse_lazy('core:lotto_activo_add')
        context['model_name'] = self.model.__name__
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminLottoActivoInterRD(ListView):
    model = LottoActivoInterRD
    template_name = "admin/erp/animalitos/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Animalitos"
        context['entity'] = 'LottoActivoInterRD'
        context['url'] = reverse_lazy('core:lottoActivoInterRD')
        context['create_url'] = reverse_lazy('core:lotto_Activo_inter_rd_add')
        context['model_name'] = self.model.__name__
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminLottoRey(ListView):
    model = LottoRey
    template_name = "admin/erp/animalitos/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Animalitos"
        context['entity'] = 'LottoRey'
        context['url'] = reverse_lazy('core:lottoRey')
        context['create_url'] = reverse_lazy('core:lotto_rey_add')
        context['model_name'] = self.model.__name__
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminSelvaPlus(ListView):
    model = SelvaPlus
    template_name = "admin/erp/animalitos/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Animalitos"
        context['entity'] = 'SelvaPlus'
        context['model_name'] = self.model.__name__
        context['url'] = reverse_lazy('core:selvaPlus')
        context['create_url'] = reverse_lazy('core:selva_plus_add')
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminGuacharoActivo(ListView):
    model = GuacharoActivo
    template_name = "admin/erp/animalitos/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Animalitos"
        context['entity'] = 'GuacharoActivo'
        context['model_name'] = self.model.__name__
        context['url'] = reverse_lazy('core:guacharoActivo')
        context['create_url'] = reverse_lazy('core:guacharo_activo_add')
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminGranjaMillonaria(ListView):
    model = GranjaMillonaria
    template_name = "admin/erp/animalitos/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Animalitos"
        context['entity'] = 'GranjaMillonaria'
        context['model_name'] = self.model.__name__
        context['url'] = reverse_lazy('core:granjaMillonaria')
        context['create_url'] = reverse_lazy('core:granja_millonaria_add')
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminGranjazo(ListView):
    model = Granjazo
    template_name = "admin/erp/animalitos/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Animalitos"
        context['entity'] = 'Granjazo'
        context['model_name'] = self.model.__name__
        context['url'] = reverse_lazy('core:granjazo')
        context['create_url'] = reverse_lazy('core:granjazo_add')
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminTerminalito(ListView):
    model = Terminalito
    template_name = "admin/erp/animalitos/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Animalitos"
        context['entity'] = 'Terminalito'
        context['model_name'] = self.model.__name__
        context['url'] = reverse_lazy('core:terminalito')
        context['create_url'] = reverse_lazy('core:terminalito_add')
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminFruitaGana(ListView):
    model = FruitaGana
    template_name = "admin/erp/animalitos/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Animalitos"
        context['entity'] = 'FruitaGana'
        context['model_name'] = self.model.__name__
        context['url'] = reverse_lazy('core:fruitaGana')
        context['create_url'] = reverse_lazy('core:fruitaGana_add')
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminGuacharito(ListView):
    model = Guacharito
    template_name = "admin/erp/animalitos/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Animalitos"
        context['entity'] = 'Guacharito'
        context['model_name'] = self.model.__name__
        context['url'] = reverse_lazy('core:guacharito')
        context['create_url'] = reverse_lazy('core:guacharito_add')
        return context


# L I S T A D O S   D E   L O T E R I A S
@method_decorator(staff_member_required, name='dispatch')
class AdminTripleCaliente(ListView):
    model = TripleCaliente
    template_name = "admin/erp/loterias/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = "Listado de Loterias"
        context['title'] = 'TripleCaliente'
        
        context['create_url'] = reverse_lazy('core:triple_caliente_add')
        context['url'] = reverse_lazy('core:triple_caliente')
        context['model_name'] = self.model.__name__
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminTripleCaracas(ListView):
    model = TripleCaracas
    template_name = "admin/erp/loterias/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = "Listado de Loterias"
        context['title']= 'TripleCaracas'
        
        context['create_url'] = reverse_lazy('core:triple_caracas_add')
        context['url'] = reverse_lazy('core:triple_caracas')
        context['model_name'] = self.model.__name__
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminTripleZulia(ListView):
    model = TripleZulia
    template_name = "admin/erp/loterias/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = "Listado de Loterias"
        context['title']= 'TripleZulia'
        
        context['create_url'] = reverse_lazy('core:triple_zulia_add')
        context['url'] = reverse_lazy('core:triple_zulia')
        context['model_name'] = self.model.__name__
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminTripleZamorano(ListView):
    model = TripleZamorano
    template_name = "admin/erp/loterias/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = "Listado de Loterias"
        context['title']= 'TripleZamorano'
        
        context['create_url'] = reverse_lazy('core:triple_zamorano_add')
        context['url'] = reverse_lazy('core:triple_zamorano')
        context['model_name'] = self.model.__name__
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminTripleChance(ListView):
    model = TripleChance
    template_name = "admin/erp/loterias/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = "Listado de Loterias"
        context['title']= 'TripleChance'
        
        context['create_url'] = reverse_lazy('core:triple_chance_add')
        context['url'] = reverse_lazy('core:triple_chance')
        context['model_name'] = self.model.__name__
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminTripleTachira(ListView):
    model = TripleTachira
    template_name = "admin/erp/loterias/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = "Listado de Loterias"
        context['title']= 'TripleTachira'
        
        context['create_url'] = reverse_lazy('core:triple_tachira_add')
        context['url'] = reverse_lazy('core:triple_tachira')
        context['model_name'] = self.model.__name__
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminTrioActivo(ListView):
    model = TrioActivo
    template_name = "admin/erp/loterias/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = "Listado de Loterias"
        context['title']= 'TrioActivo'
        
        context['create_url'] = reverse_lazy('core:trio_activo_add')
        context['url'] = reverse_lazy('core:trio_activo')
        context['model_name'] = self.model.__name__
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminRicachona(ListView):
    model = Ricachona
    template_name = "admin/erp/loterias/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = "Listado de Loterias"
        context['title']= 'Ricachona'
        
        context['create_url'] = reverse_lazy('core:la_ricachona_add')
        context['url'] = reverse_lazy('core:ricachona')
        context['model_name'] = self.model.__name__
        return context


@method_decorator(staff_member_required, name='dispatch')
class VideoModelTodayListView(ListView):
    model = VideoModelToday
    template_name = "admin/erp/upload/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = "Listado de Videos"
        context['title']= 'Videos'
        
        context['create_url'] = reverse_lazy('core:videos_upload')
        context['url'] = reverse_lazy('core:videos_list')
        context['model_name'] = self.model.__name__
        return context


#  I N G R E S O   D E   A N I M A L I T O S   P O R   H O R A R I O S
@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class AddGroupResultA(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en los modelos correspondientes
            for model_name, form_data in data.items():
                if model_name == 'LaGranjita':
                    model = LaGranjita
                elif model_name == 'GuacharoActivo':
                    model = GuacharoActivo
                elif model_name == 'SelvaPlus':
                    model = SelvaPlus
                if(form_data['save']):
                    # Crear una nueva instancia del modelo y guardarla
                    instance = model(hour_sort=form_data['hour'], animalito=form_data['animal'])
                    instance.full_clean()  # Validar la instancia
                    instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'Los modelos se han guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Animalitos"
        context['title'] = 'La Granjita-SelvaPlus-Guacharo Activo'
        # Crear una lista con los nombres de los modelos
        model_names = ['LaGranjita', 'SelvaPlus', 'GuacharoActivo']
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices de cada modelo
        models = []
        for model_name in model_names:
            if model_name == 'LaGranjita':
                model = LaGranjita
            elif model_name == 'SelvaPlus':
                model = SelvaPlus
            elif model_name == 'GuacharoActivo':
                model = GuacharoActivo

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'animalito_choices': model._meta.get_field('animalito').choices,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/animalitos/group_result_add.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class AddGroupResultB(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en los modelos correspondientes
            for model_name, form_data in data.items():
                if model_name == 'GranjaPlus':
                    model = GranjaPlus
                elif model_name == 'LottoActivoInterRD':
                    model = LottoActivoInterRD
                elif model_name == 'LottoRey':
                    model = LottoRey
                elif model_name == 'Guacharito':  # <-- Añade esta línea
                    model = Guacharito

                if(form_data['save']):
                    # Crear una nueva instancia del modelo y guardarla
                    instance = model(hour_sort=form_data['hour'], animalito=form_data['animal'])
                    instance.full_clean()  # Validar la instancia
                    instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'Los modelos se han guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Animalitos"
        context['title'] = 'GranjaPlus-Lotto Activo Inter RD-Lotto Rey-Guacharito'  # <-- Actualiza el título si quieres
        # Crear una lista con los nombres de los modelos
        model_names = ['GranjaPlus', 'LottoActivoInterRD', 'LottoRey', 'Guacharito']  # <-- Añade Guacharito
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices de cada modelo
        models = []
        for model_name in model_names:
            if model_name == 'GranjaPlus':
                model = GranjaPlus
            elif model_name == 'LottoActivoInterRD':
                model = LottoActivoInterRD
            elif model_name == 'LottoRey':
                model = LottoRey
            elif model_name == 'Guacharito':  # <-- Añade esta línea
                model = Guacharito

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'animalito_choices': model._meta.get_field('animalito').choices,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/animalitos/group_result_add.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class AddGroupResultC(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en los modelos correspondientes
            for model_name, form_data in data.items():
                if model_name == 'ChanceAnimalitos':
                    model = ChanceAnimalitos
                elif model_name == 'LottoActivo':
                    model = LottoActivo
                elif model_name == 'GranjaMillonaria':
                    model = GranjaMillonaria

                if(form_data['save']):
                    # Crear una nueva instancia del modelo y guardarla
                    instance = model(hour_sort=form_data['hour'], animalito=form_data['animal'])
                    instance.full_clean()  # Validar la instancia
                    instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'Los modelos se han guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Animalitos"
        context['title'] = 'Chance Animalitos-Lotto Activo-Granja Millonaria'
        # Crear una lista con los nombres de los modelos
        model_names = ['ChanceAnimalitos', 'LottoActivo', 'GranjaMillonaria']
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices de cada modelo
        models = []
        for model_name in model_names:
            if model_name == 'ChanceAnimalitos':
                model = ChanceAnimalitos
            elif model_name == 'LottoActivo':
                model = LottoActivo
            elif model_name == 'GranjaMillonaria':
                model = GranjaMillonaria

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'animalito_choices': model._meta.get_field('animalito').choices,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/animalitos/group_result_add.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class AddGroupResultD(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'LaRicachona':
                    model = LaRicachona

                if(form_data['save']):
                    # Crear una nueva instancia del modelo y guardarla
                    instance = model(hour_sort=form_data['hour'], animalito=form_data['animal'])
                    instance.full_clean()  # Validar la instancia
                    instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Animalitos"
        context['title'] = 'La Ricachona'
        # Crear una lista con el nombre del modelo
        model_names = ['LaRicachona']
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices del modelo
        models = []
        for model_name in model_names:
            if model_name == 'LaRicachona':
                model = LaRicachona

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'animalito_choices': model._meta.get_field('animalito').choices,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/animalitos/group_result_add.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class AddGroupResultE(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'Granjazo':
                    model = Granjazo

                if(form_data['save']):
                    # Crear una nueva instancia del modelo y guardarla
                    instance = model(hour_sort=form_data['hour'], animalito=form_data['animal'])
                    instance.full_clean()  # Validar la instancia
                    instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Animalitos"
        context['title'] = 'Granjazo'
        # Crear una lista con el nombre del modelo
        model_names = ['Granjazo']
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices del modelo
        models = []
        for model_name in model_names:
            if model_name == 'Granjazo':
                model = Granjazo

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'animalito_choices': model._meta.get_field('animalito').choices,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/animalitos/group_result_add.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class AddGroupResultF(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'Terminalito':
                    model = Terminalito

                if(form_data['save']):
                    # Crear una nueva instancia del modelo y guardarla
                    instance = model(hour_sort=form_data['hour'], animalito=form_data['animal'])
                    instance.full_clean()  # Validar la instancia
                    instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Animalitos"
        context['title'] = 'Terminalito'
        # Crear una lista con el nombre del modelo
        model_names = ['Terminalito']
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices del modelo
        models = []
        for model_name in model_names:
            if model_name == 'Terminalito':
                model = Terminalito

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'animalito_choices': model._meta.get_field('animalito').choices,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/animalitos/group_result_add.html', context)

# I N G R E S O   D E   L O T E R I A S   P O R   H O R A R I O S 

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class AddLoteryGroupResultA(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)
        print(data)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'TripleCaliente':
                    model = TripleCaliente

                if(form_data['save']):
                    # Crear una nueva instancia del modelo y guardarla
                    instance = model(hour_sort=form_data['hour'], a=form_data['a'], b=form_data['b'], c=form_data['c'], zod=form_data['zod'])
                    instance.full_clean()  # Validar la instancia
                    instance.save()
            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Loterias"
        context['title'] = 'TripleCaliente'
        # Crear una lista con el nombre del modelo
        model_names = ['TripleCaliente']
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices del modelo
        models = []
        for model_name in model_names:
            if model_name == 'TripleCaliente':
                model = TripleCaliente

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'hour_sort_choices': hour_sort_choices,
                'zod_choices': model._meta.get_field('zod').choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/loterias/group_result_add.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class AddLoteryGroupResultB(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en los modelos correspondientes
            for model_name, form_data in data.items():
                if model_name == 'TripleCaracas':
                    model = TripleCaracas
                elif model_name == 'TripleChance':
                    model = TripleChance
                
                if(form_data['save']):
                    # Crear una nueva instancia del modelo y guardarla
                    instance = model(hour_sort=form_data['hour'], a=form_data['a'], b=form_data['b'], c=form_data['c'], zod=form_data['zod'])
                    instance.full_clean()  # Validar la instancia
                    instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'Los modelos se han guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Loterias"
        context['title'] = 'TripleCaracas-TripleChance'
        # Crear una lista con los nombres de los modelos
        model_names = ['TripleCaracas', 'TripleChance']
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices de cada modelo
        models = []
        for model_name in model_names:
            if model_name == 'TripleCaracas':
                model = TripleCaracas
            elif model_name == 'TripleChance':
                model = TripleChance

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'hour_sort_choices': hour_sort_choices,
                'zod_choices': model._meta.get_field('zod').choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/loterias/group_result_add.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class AddLoteryGroupResultC(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en los modelos correspondientes
            for model_name, form_data in data.items():
                if model_name == 'TripleZulia':
                    model = TripleZulia

                
                if(form_data['save']):
                    # Crear una nueva instancia del modelo y guardarla
                    instance = model(hour_sort=form_data['hour'], a=form_data['a'], b=form_data['b'], c=form_data['c'], zod=form_data['zod'])
                    instance.full_clean()  # Validar la instancia
                    instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'Los modelos se han guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Loterias"
        context['title'] = 'TripleZulia'
        # Crear una lista con los nombres de los modelos
        model_names = ['TripleZulia']
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices de cada modelo
        models = []
        for model_name in model_names:
            if model_name == 'TripleZulia':
                model = TripleZulia

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'hour_sort_choices': hour_sort_choices,
                'zod_choices': model._meta.get_field('zod').choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/loterias/group_result_add.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class AddLoteryGroupResultD(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en los modelos correspondientes
            for model_name, form_data in data.items():
                if model_name == 'TripleZamorano':
                    model = TripleZamorano

                if(form_data['save']):
                    # Crear una nueva instancia del modelo y guardarla
                    instance = model(hour_sort=form_data['hour'], a=form_data['a'], c=form_data['c'], zod=form_data['zod'])
                    instance.full_clean()  # Validar la instancia
                    instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'Los modelos se han guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Loterias"
        context['title'] = 'TripleZamorano'
        # Crear una lista con los nombres de los modelos
        model_names = ['TripleZamorano']
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices de cada modelo
        models = []
        for model_name in model_names:
            if model_name == 'TripleZamorano':
                model = TripleZamorano

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'hour_sort_choices': hour_sort_choices,
                'zod_choices': model._meta.get_field('zod').choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/loterias/group_result_add.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class AddLoteryGroupResultE(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en los modelos correspondientes
            for model_name, form_data in data.items():
                if model_name == 'TripleTachira':
                    model = TripleTachira


                if(form_data['save']):
                    # Crear una nueva instancia del modelo y guardarla
                    instance = model(hour_sort=form_data['hour'], a=form_data['a'], b=form_data['b'], c=form_data['c'], zod=form_data['zod'])
                    instance.full_clean()  # Validar la instancia
                    instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'Los modelos se han guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Loterias"
        context['title'] = 'TripleTachira'
        # Crear una lista con los nombres de los modelos
        model_names = ['TripleTachira']
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices de cada modelo
        models = []
        for model_name in model_names:
            if model_name == 'TripleTachira':
                model = TripleTachira

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'hour_sort_choices': hour_sort_choices,
                'zod_choices': model._meta.get_field('zod').choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/loterias/group_result_add.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class AddLoteryGroupResultF(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en los modelos correspondientes
            for model_name, form_data in data.items():
                if model_name == 'TrioActivo':
                    model = TrioActivo

                if(form_data['save']):
                    # Crear una nueva instancia del modelo y guardarla
                    instance = model(hour_sort=form_data['hour'], a=form_data['a'])
                    instance.full_clean()  # Validar la instancia
                    instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'Los modelos se han guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Loterias"
        context['title'] = 'TrioActivo'
        # Crear una lista con los nombres de los modelos
        model_names = ['TrioActivo']
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices de cada modelo
        models = []
        for model_name in model_names:
            if model_name == 'TrioActivo':
                model = TrioActivo

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/loterias/group_result_add.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class AddLoteryGroupResultG(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en los modelos correspondientes
            for model_name, form_data in data.items():
                if model_name == 'Ricachona':
                    model = Ricachona

                if(form_data['save']):
                    # Crear una nueva instancia del modelo y guardarla
                    instance = model(hour_sort=form_data['hour'], a=form_data['a'])
                    instance.full_clean()  # Validar la instancia
                    instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'Los modelos se han guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Loterias"
        context['title'] = 'Ricachona'
        # Crear una lista con los nombres de los modelos
        model_names = ['Ricachona']
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices de cada modelo
        models = []
        for model_name in model_names:
            if model_name == 'Ricachona':
                model = Ricachona

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/loterias/group_result_add.html', context)


# I N G R E S O   D E  A N I M A L I T O S    I N D I V I D U A L
@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class ChanceAnimalitosView(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'ChanceAnimalitos':
                    model = ChanceAnimalitos

                # Crear una nueva instancia del modelo y guardarla
                instance = model(hour_sort=form_data['hour'], animalito=form_data['animal'])
                instance.full_clean()  # Validar la instancia
                instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Animalitos"
        context['title'] = 'ChanceAnimalitos'
        context['url'] = reverse_lazy('core:chanceAnimalitos')
        # Crear una lista con el nombre del modelo
        model_names = ['ChanceAnimalitos']
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices del modelo
        models = []
        for model_name in model_names:
            if model_name == 'ChanceAnimalitos':
                model = ChanceAnimalitos

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'animalito_choices': model._meta.get_field('animalito').choices,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/animalitos/add_individual.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class GranjaPlusView(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'GranjaPlus':
                    model = GranjaPlus

                # Crear una nueva instancia del modelo y guardarla
                instance = model(hour_sort=form_data['hour'], animalito=form_data['animal'])
                instance.full_clean()  # Validar la instancia
                instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Animalitos"
        context['title'] = 'GranjaPlus'
        # Crear una lista con el nombre del modelo
        model_names = ['GranjaPlus']
        context['url'] = reverse_lazy('core:granjaPlus')
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices del modelo
        models = []
        for model_name in model_names:
            if model_name == 'GranjaPlus':
                model = GranjaPlus

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'animalito_choices': model._meta.get_field('animalito').choices,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/animalitos/add_individual.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class LaGranjitaView(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'LaGranjita':
                    model = LaGranjita

                # Crear una nueva instancia del modelo y guardarla
                instance = model(hour_sort=form_data['hour'], animalito=form_data['animal'])
                instance.full_clean()  # Validar la instancia
                instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Animalitos"
        context['title'] = 'LaGranjita'
        context['url'] = reverse_lazy('core:laGranjita')
        # Crear una lista con el nombre del modelo
        model_names = ['LaGranjita']
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices del modelo
        models = []
        for model_name in model_names:
            if model_name == 'LaGranjita':
                model = LaGranjita

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'animalito_choices': model._meta.get_field('animalito').choices,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/animalitos/add_individual.html', context)


@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class LaRicachonaView(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'LaRicachona':
                    model = LaRicachona

                # Crear una nueva instancia del modelo y guardarla
                instance = model(hour_sort=form_data['hour'], animalito=form_data['animal'])
                instance.full_clean()  # Validar la instancia
                instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Animalitos"
        context['title'] = 'LaRicachona'
        context['url'] = reverse_lazy('core:laRicachona')
        # Crear una lista con el nombre del modelo
        model_names = ['LaRicachona']
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices del modelo
        models = []
        for model_name in model_names:
            if model_name == 'LaRicachona':
                model = LaRicachona

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'animalito_choices': model._meta.get_field('animalito').choices,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/animalitos/add_individual.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class LottoActivoView(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'LottoActivo':
                    model = LottoActivo

                # Crear una nueva instancia del modelo y guardarla
                instance = model(hour_sort=form_data['hour'], animalito=form_data['animal'])
                instance.full_clean()  # Validar la instancia
                instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Animalitos"
        context['title'] = 'LottoActivo'
        context['url'] = reverse_lazy('core:lottoActivo')
        # Crear una lista con el nombre del modelo
        model_names = ['LottoActivo']
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices del modelo
        models = []
        for model_name in model_names:
            if model_name == 'LottoActivo':
                model = LottoActivo

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'animalito_choices': model._meta.get_field('animalito').choices,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/animalitos/group_result_add.html', context)


@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class LottoActivoInterRDView(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'LottoActivoInterRD':
                    model = LottoActivoInterRD

                # Crear una nueva instancia del modelo y guardarla
                instance = model(hour_sort=form_data['hour'], animalito=form_data['animal'])
                instance.full_clean()  # Validar la instancia
                instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Animalitos"
        context['title'] = 'LottoActivoInterRD'
        context['url'] = reverse_lazy('core:lottoActivoInterRD')
        # Crear una lista con el nombre del modelo
        model_names = ['LottoActivoInterRD']
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices del modelo
        models = []
        for model_name in model_names:
            if model_name == 'LottoActivoInterRD':
                model = LottoActivoInterRD

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'animalito_choices': model._meta.get_field('animalito').choices,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/animalitos/add_individual.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class LottoReyView(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'LottoRey':
                    model = LottoRey

                # Crear una nueva instancia del modelo y guardarla
                instance = model(hour_sort=form_data['hour'], animalito=form_data['animal'])
                instance.full_clean()  # Validar la instancia
                instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Animalitos"
        context['title'] = 'LottoRey'
        context['url'] = reverse_lazy('core:lottoRey')
        # Crear una lista con el nombre del modelo
        model_names = ['LottoRey']
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices del modelo
        models = []
        for model_name in model_names:
            if model_name == 'LottoRey':
                model = LottoRey

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'animalito_choices': model._meta.get_field('animalito').choices,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/animalitos/add_individual.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class SelvaPlusView(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'SelvaPlus':
                    model = SelvaPlus

                # Crear una nueva instancia del modelo y guardarla
                instance = model(hour_sort=form_data['hour'], animalito=form_data['animal'])
                instance.full_clean()  # Validar la instancia
                instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Animalitos"
        context['title'] = 'SelvaPlus'
        context['url'] = reverse_lazy('core:selvaPlus')
        # Crear una lista con el nombre del modelo
        model_names = ['SelvaPlus']
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices del modelo
        models = []
        for model_name in model_names:
            if model_name == 'SelvaPlus':
                model = SelvaPlus

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'animalito_choices': model._meta.get_field('animalito').choices,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/animalitos/add_individual.html', context)


@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class GuacharoActivoView(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'GuacharoActivo':
                    model = GuacharoActivo

                # Crear una nueva instancia del modelo y guardarla
                instance = model(hour_sort=form_data['hour'], animalito=form_data['animal'])
                instance.full_clean()  # Validar la instancia
                instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Animalitos"
        context['title'] = 'GuacharoActivo'
        context['url'] = reverse_lazy('core:guacharoActivo')
        # Crear una lista con el nombre del modelo
        model_names = ['GuacharoActivo']
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices del modelo
        models = []
        for model_name in model_names:
            if model_name == 'GuacharoActivo':
                model = GuacharoActivo

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'animalito_choices': model._meta.get_field('animalito').choices,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/animalitos/add_individual.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class GranjaMillonariaView(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'GranjaMillonaria':
                    model = GranjaMillonaria

                # Crear una nueva instancia del modelo y guardarla
                instance = model(hour_sort=form_data['hour'], animalito=form_data['animal'])
                instance.full_clean()  # Validar la instancia
                instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Animalitos"
        context['title'] = 'GranjaMillonaria'
        context['url'] = reverse_lazy('core:granjaMillonaria')
        # Crear una lista con el nombre del modelo
        model_names = ['GranjaMillonaria']
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices del modelo
        models = []
        for model_name in model_names:
            if model_name == 'GranjaMillonaria':
                model = GranjaMillonaria

            # Filtrar los registros de hoy
            today = date.today()
            today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
            today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
            hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

            models.append({
                'name': model_name,
                'animalito_choices': model._meta.get_field('animalito').choices,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/animalitos/add_individual.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class GranjazoView(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'Granjazo':
                    model = Granjazo

                # Crear una nueva instancia del modelo y guardarla
                instance = model(hour_sort=form_data['hour'], animalito=form_data['animal'])
                instance.full_clean()  # Validar la instancia
                instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Animalitos"
        context['title'] = 'Granjazo'
        context['url'] = reverse_lazy('core:granjazo')
        # Crear una lista con el nombre del modelo
        model_names = 'Granjazo'
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices del modelo
        model = Granjazo
        models = []
        # Filtrar los registros de hoy
        today = date.today()
        today_records = model.objects.filter(date_sort=today)

        # Obtener los horarios que ya se han registrado hoy
        today_hours = [record.hour_sort for record in today_records]

        # Excluir estos horarios al crear tus choices
        hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

        models.append({
                'name': model_names,
                'animalito_choices': model._meta.get_field('animalito').choices,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/animalitos/add_individual.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class TerminalitoView(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'Terminalito':
                    model = Terminalito

                # Crear una nueva instancia del modelo y guardarla
                instance = model(hour_sort=form_data['hour'], animalito=form_data['animal'])
                instance.full_clean()  # Validar la instancia
                instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Animalitos"
        context['title'] = 'Terminalito'
        context['url'] = reverse_lazy('core:terminalito')
        # Crear una lista con el nombre del modelo
        model_names = 'Terminalito'
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices del modelo
        model = Terminalito
        models = []
        # Filtrar los registros de hoy
        today = date.today()
        today_records = model.objects.filter(date_sort=today)

        # Obtener los horarios que ya se han registrado hoy
        today_hours = [record.hour_sort for record in today_records]

        # Excluir estos horarios al crear tus choices
        hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

        models.append({
                'name': model_names,
                'animalito_choices': model._meta.get_field('animalito').choices,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/animalitos/add_individual.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class FruitaGanaView(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'FruitaGana':
                    model = FruitaGana

                # Crear una nueva instancia del modelo y guardarla
                instance = model(hour_sort=form_data['hour'], animalito=form_data['animal'])
                instance.full_clean()  # Validar la instancia
                instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Animalitos"
        context['title'] = 'FruitaGana'
        context['url'] = reverse_lazy('core:fruitaGana')
        # Crear una lista con el nombre del modelo
        model_names = 'FruitaGana'
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices del modelo
        model = FruitaGana
        models = []
        # Filtrar los registros de hoy
        today = date.today()
        today_records = model.objects.filter(date_sort=today)

        # Obtener los horarios que ya se han registrado hoy
        today_hours = [record.hour_sort for record in today_records]

        # Excluir estos horarios al crear tus choices
        hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

        models.append({
                'name': model_names,
                'animalito_choices': model._meta.get_field('animalito').choices,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/animalitos/add_individual.html', context)


@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class GuacharitoView(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'Guacharito':
                    model = Guacharito

                # Crear una nueva instancia del modelo y guardarla
                instance = model(hour_sort=form_data['hour'], animalito=form_data['animal'])
                instance.full_clean()  # Validar la instancia
                instance.save()

            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Animalitos"
        context['title'] = 'Guacharito'
        context['url'] = reverse_lazy('core:guacharito')
        # Crear una lista con el nombre del modelo
        model_names = 'Guacharito'
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_names

        # Crear una lista de diccionarios con los choices del modelo
        model = Guacharito
        models = []
        # Filtrar los registros de hoy
        today = date.today()
        today_records = model.objects.filter(date_sort=today)

        # Obtener los horarios que ya se han registrado hoy
        today_hours = [record.hour_sort for record in today_records]

        # Excluir estos horarios al crear tus choices
        hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

        models.append({
                'name': model_names,
                'animalito_choices': model._meta.get_field('animalito').choices,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/animalitos/add_individual.html', context)

# I N G R E S O   D E  L O T E R I A S  I N D I V I D U A L
@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class TripleCalienteView(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)
        print(data)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'TripleCaliente':
                    model = TripleCaliente

                # Crear una nueva instancia del modelo y guardarla
                instance = model(hour_sort=form_data['hour'], a=form_data['a'], b=form_data['b'], c=form_data['c'], zod=form_data['zod'])
                instance.full_clean()  # Validar la instancia
                instance.save()
            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Loterias"
        context['title'] = 'TripleCaliente'
        context['url'] = reverse_lazy('core:triple_caliente')
        # Crear una lista con el nombre del modelo
        model_name = 'TripleCaliente'
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_name

        # Crear una lista de diccionarios con los choices del modelo
        models = []
        model = TripleCaliente

            # Filtrar los registros de hoy
        today = date.today()
        today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
        today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
        hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

        models.append({
                'name': model_name,
                'hour_sort_choices': hour_sort_choices,
                'zod_choices': model._meta.get_field('zod').choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/loterias/individual_add.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class TripleCaracasView(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)
        print(data)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'TripleCaracas':
                    model = TripleCaracas

                # Crear una nueva instancia del modelo y guardarla
                instance = model(hour_sort=form_data['hour'], a=form_data['a'], b=form_data['b'], c=form_data['c'], zod=form_data['zod'])
                instance.full_clean()  # Validar la instancia
                instance.save()
            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Loterias"
        context['title'] = 'TripleCaracas'
        context['url'] = reverse_lazy('core:triple_caracas')
        # Crear una lista con el nombre del modelo
        model_name = 'TripleCaracas'
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_name

        # Crear una lista de diccionarios con los choices del modelo
        models = []
        model = TripleCaracas

            # Filtrar los registros de hoy
        today = date.today()
        today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
        today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
        hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

        models.append({
                'name': model_name,
                'hour_sort_choices': hour_sort_choices,
                'zod_choices': model._meta.get_field('zod').choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/loterias/individual_add.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class TripleZuliaView(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)
        print(data)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'TripleZulia':
                    model = TripleZulia

                # Crear una nueva instancia del modelo y guardarla
                instance = model(hour_sort=form_data['hour'], a=form_data['a'], b=form_data['b'], c=form_data['c'], zod=form_data['zod'])
                instance.full_clean()  # Validar la instancia
                instance.save()
            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Loterias"
        context['title'] = 'TripleZulia'
        context['url'] = reverse_lazy('core:triple_zulia')
        # Crear una lista con el nombre del modelo
        model_name = 'TripleZulia'
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_name

        # Crear una lista de diccionarios con los choices del modelo
        models = []
        model = TripleZulia

            # Filtrar los registros de hoy
        today = date.today()
        today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
        today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
        hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

        models.append({
                'name': model_name,
                'hour_sort_choices': hour_sort_choices,
                'zod_choices': model._meta.get_field('zod').choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/loterias/individual_add.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class TripleZamoranoView(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)
        print(data)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'TripleZamorano':
                    model = TripleZamorano

                # Crear una nueva instancia del modelo y guardarla
                instance = model(hour_sort=form_data['hour'], a=form_data['a'], c=form_data['c'], zod=form_data['zod'])
                instance.full_clean()  # Validar la instancia
                instance.save()
            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Loterias"
        context['title'] = 'TripleZamorano'
        # Crear una lista con el nombre del modelo
        model_name = 'TripleZamorano'
        context['url'] = reverse_lazy('core:triple_zamorano')
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_name

        # Crear una lista de diccionarios con los choices del modelo
        models = []
        model = TripleZamorano

            # Filtrar los registros de hoy
        today = date.today()
        today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
        today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
        hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

        models.append({
                'name': model_name,
                'hour_sort_choices': hour_sort_choices,
                'zod_choices': model._meta.get_field('zod').choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/loterias/individual_add.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class TripleChanceView(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)
        print(data)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'TripleChance':
                    model = TripleChance

                # Crear una nueva instancia del modelo y guardarla
                instance = model(hour_sort=form_data['hour'], a=form_data['a'], b=form_data['b'], c=form_data['c'], zod=form_data['zod'])
                instance.full_clean()  # Validar la instancia
                instance.save()
            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Loterias"
        context['title'] = 'TripleChance'
        context['url'] = reverse_lazy('core:triple_chance')
        # Crear una lista con el nombre del modelo
        model_name = 'TripleChance'
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_name

        # Crear una lista de diccionarios con los choices del modelo
        models = []
        model = TripleChance

            # Filtrar los registros de hoy
        today = date.today()
        today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
        today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
        hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

        models.append({
                'name': model_name,
                'hour_sort_choices': hour_sort_choices,
                'zod_choices': model._meta.get_field('zod').choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/loterias/individual_add.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class TripleTachiraView(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)
        print(data)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'TripleTachira':
                    model = TripleTachira

                # Crear una nueva instancia del modelo y guardarla
                instance = model(hour_sort=form_data['hour'], a=form_data['a'], b=form_data['b'], c=form_data['c'], zod=form_data['zod'])
                instance.full_clean()  # Validar la instancia
                instance.save()
            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Loterias"
        context['title'] = 'TripleTachira'
        context['url'] = reverse_lazy('core:triple_tachira')
        # Crear una lista con el nombre del modelo
        model_name = 'TripleTachira'
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_name

        # Crear una lista de diccionarios con los choices del modelo
        models = []
        model = TripleTachira

            # Filtrar los registros de hoy
        today = date.today()
        today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
        today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
        hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

        models.append({
                'name': model_name,
                'hour_sort_choices': hour_sort_choices,
                'zod_choices': model._meta.get_field('zod').choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/loterias/individual_add.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class TrioActivoView(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)
        print(data)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'TrioActivo':
                    model = TrioActivo

                # Crear una nueva instancia del modelo y guardarla
                instance = model(hour_sort=form_data['hour'], a=form_data['a'], )
                instance.full_clean()  # Validar la instancia
                instance.save()
            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Loterias"
        context['title'] = 'TrioActivo'
        context['url'] = reverse_lazy('core:trio_activo')
        # Crear una lista con el nombre del modelo
        model_name = 'TrioActivo'
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_name

        # Crear una lista de diccionarios con los choices del modelo
        models = []
        model = TrioActivo

            # Filtrar los registros de hoy
        today = date.today()
        today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
        today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
        hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

        models.append({
                'name': model_name,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/loterias/individual_add.html', context)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class RicachonaView(View):
    def post(self, request):
        # Recibir los datos de los formularios
        data = json.loads(request.body)

        try:
            # Validar los datos y guardarlos en el modelo correspondiente
            for model_name, form_data in data.items():
                if model_name == 'Ricachona':
                    model = Ricachona

                # Crear una nueva instancia del modelo y guardarla
                instance = model(hour_sort=form_data['hour'], a=form_data['a'])
                instance.full_clean()  # Validar la instancia
                instance.save()
            # Devolver una respuesta de éxito al cliente
            return JsonResponse({'status': 'success', 'message': 'El modelo se ha guardado correctamente.'})

        except ValidationError as e:
            # Devolver una respuesta de error al cliente
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    def get(self, request):
        context = {}
        context['entity'] = "Registro de Loterias"
        context['title'] = 'Ricachona'
        context['url'] = reverse_lazy('core:ricachona')
        # Crear una lista con el nombre del modelo
        model_name = 'Ricachona'
        # Asignar la lista al contexto con el nombre 'model'
        context['model'] = model_name

        # Crear una lista de diccionarios con los choices del modelo
        models = []
        model = Ricachona

            # Filtrar los registros de hoy
        today = date.today()
        today_records = model.objects.filter(date_sort=today)

            # Obtener los horarios que ya se han registrado hoy
        today_hours = [record.hour_sort for record in today_records]

            # Excluir estos horarios al crear tus choices
        hour_sort_choices = [choice for choice in model._meta.get_field('hour_sort').choices if choice[0] not in today_hours]

        models.append({
                'name': model_name,
                'hour_sort_choices': hour_sort_choices,
            })

        context['models'] = models

        return render(request, 'admin/erp/loterias/individual_add.html', context)

@method_decorator(staff_member_required, name='dispatch')
class UploadVideo(CreateView):
    model = VideoModelToday
    fields = '__all__'
    template_name = 'admin/erp/upload/videos.html'  # Nombre de tu template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = "Pestaña de videos - Registro de Videos"
        context['title'] = 'Videos'
        context['url'] = reverse_lazy('core:videos_upload')

        # No llamamos al método super().get() para evitar renderizar el formulario
        return context

# V I S T A S   D E  U S U A R I O S
@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class RegisterUserView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'admin/erp/users/registration.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'El usuario se ha guardado correctamente.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'El usuario No se ha podido registrar.'})

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class UserListView(ListView):
    model = User
    template_name = 'admin/erp/users/user_list.html'  # Cambia esto a la ruta de tu plantilla
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = "Listado de Usuarios"
        context['title']= 'Usuarios'
        
        context['create_url'] = reverse_lazy('core:user_register')
        context['url'] = reverse_lazy('core:user_register')
        context['model_name'] = self.model.__name__
        return context

# VISTAS AJAX
@csrf_exempt
def ajax_delete_view(request):
    id = request.POST.get('id')
    model_name = request.POST.get('model_name')
    Model = apps.get_model('core', model_name)
    try:
        object = Model.objects.get(id=id)
        object.delete()
        return JsonResponse({'success': True})
    except Model.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Object does not exist'})

@csrf_exempt
def upload_video(request):
    if request.method == 'POST':
        video = request.FILES['video']
        name = request.POST['name']
        try:
            video_to_delete = VideoModel.objects.get(name=name)
            os.remove(os.path.join(settings.MEDIA_ROOT, str(video_to_delete.video)))
            video_to_delete.delete()
        except VideoModel.DoesNotExist:
            pass

        video_model = VideoModel(name=name, video=video)
        video_model.save()

        return JsonResponse({'message': 'Video Subido con exito!'})
    else:
        return JsonResponse({'error': 'Invalid request'})

@csrf_exempt
def delete_video(request):
    if request.method == 'POST':
        name = request.POST['name']
        try:
            video_to_delete = VideoModel.objects.get(name=name)
            os.remove(os.path.join(settings.MEDIA_ROOT, str(video_to_delete.video)))
            video_to_delete.delete()
            return JsonResponse({'message': 'Video eliminado satisfactoriamente!'})
        except VideoModel.DoesNotExist:
            return JsonResponse({'error': 'Video no existe'})
    else:
        return JsonResponse({'error': 'Invalid request'})

@csrf_exempt
def upload_video_today_page(request):
    if request.method == 'POST':
        video = request.FILES['video']
        video_model = VideoModelToday(video=video)
        video_model.save()

        return JsonResponse({'message': 'Video Subido con exito!'})
    else:
        return JsonResponse({'error': 'Invalid request'})

@csrf_exempt
def update_time_pages(request):
    if request.method == 'POST':
        try:
            new_time_seconds = int(request.POST.get('time'))  # Obtén el valor del tiempo en segundos
            new_time_milliseconds = new_time_seconds * 1000  # Convierte a milisegundos
            time_view = TimeView.objects.first()  # Obtén el único registro
            time_view.time_in_milliseconds = new_time_milliseconds
            time_view.save()  # Guarda los cambios en la base de datos
            return JsonResponse({'message': 'Tiempo actualizado con éxito!'})
        except ValueError:
            return JsonResponse({'error': 'Valor de tiempo no válido'})
    else:
        return JsonResponse({'error': 'Solicitud inválida'})