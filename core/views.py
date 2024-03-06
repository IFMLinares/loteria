import json
from datetime import time, date, timedelta
from collections import defaultdict
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, ListView
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from .models import *
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

class LotteryView(View):
    def get(self, request):
        context = ContextData(date.today())
        context['yesterday'] = ContextData(date.today() - timedelta(days=1))
        print(context)
        return render(request, 'lotoview/index.html', context)


@method_decorator(staff_member_required, name='dispatch')
class IndexView(View):
    def get(self, request):
        context = {}
        context['title'] = "Inicio"
        context['entity'] = 'Pagina de inicio'

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
        context['create_url'] = reverse_lazy('core:lottery')
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
        context['create_url'] = reverse_lazy('core:lottery')
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
        context['create_url'] = reverse_lazy('core:lottery')
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
        context['create_url'] = reverse_lazy('core:lottery')
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
        context['create_url'] = reverse_lazy('core:lottery')
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
        context['create_url'] = reverse_lazy('core:lottery')
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
        context['create_url'] = reverse_lazy('core:lottery')
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
        context['create_url'] = reverse_lazy('core:lottery')
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
        context['create_url'] = reverse_lazy('core:lottery')
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
        context['create_url'] = reverse_lazy('core:lottery')
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
        context['create_url'] = reverse_lazy('core:lottery')
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminTripleCaliente(ListView):
    model = TripleCaliente
    template_name = "admin/erp/loterias/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = "Listado de Loerias"
        context['title'] = 'TripleCaliente'
        context['create_url'] = reverse_lazy('core:lottery')
        context['model_name'] = self.model.__name__
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminTripleCaracas(ListView):
    model = TripleCaracas
    template_name = "admin/erp/loterias/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = "Listado de Loerias"
        context['title']= 'TripleCaracas'
        context['create_url'] = reverse_lazy('core:lottery')
        context['model_name'] = self.model.__name__
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminTripleZulia(ListView):
    model = TripleZulia
    template_name = "admin/erp/loterias/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = "Listado de Loerias"
        context['title']= 'TripleZulia'
        context['create_url'] = reverse_lazy('core:lottery')
        context['model_name'] = self.model.__name__
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminTripleZamorano(ListView):
    model = TripleZamorano
    template_name = "admin/erp/loterias/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = "Listado de Loerias"
        context['title']= 'TripleZamorano'
        context['create_url'] = reverse_lazy('core:lottery')
        context['model_name'] = self.model.__name__
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminTripleChance(ListView):
    model = TripleChance
    template_name = "admin/erp/loterias/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = "Listado de Loerias"
        context['title']= 'TripleChance'
        context['create_url'] = reverse_lazy('core:lottery')
        context['model_name'] = self.model.__name__
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminTripleTachira(ListView):
    model = TripleTachira
    template_name = "admin/erp/loterias/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = "Listado de Loerias"
        context['title']= 'TripleTachira'
        context['create_url'] = reverse_lazy('core:lottery')
        context['model_name'] = self.model.__name__
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminTrioActivo(ListView):
    model = TrioActivo
    template_name = "admin/erp/loterias/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = "Listado de Loerias"
        context['title']= 'TrioActivo'
        context['create_url'] = reverse_lazy('core:lottery')
        context['model_name'] = self.model.__name__
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminRicachona(ListView):
    model = Ricachona
    template_name = "admin/erp/loterias/list-view.html"
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = "Listado de Loerias"
        context['title']= 'Ricachona'
        context['create_url'] = reverse_lazy('core:lottery')
        context['model_name'] = self.model.__name__
        return context

# Ingreso de Resultados Agrupados por horarios

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
        context['title'] = 'GranjaPlus-Lotto Activo Inter RD-Lotto Rey'
        # Crear una lista con los nombres de los modelos
        model_names = ['GranjaPlus', 'LottoActivoInterRD', 'LottoRey']
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
