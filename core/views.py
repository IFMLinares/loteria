from datetime import time, date, timedelta
from collections import defaultdict
from django.shortcuts import render
from django.views.generic import View
from django.utils import timezone
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
                elif model_name in ['TripleCaliente', 'TripleCaracas', 'TripleZulia', 'TripleZamorano', 'TripleChance', 'TripleTachira']:
                    context[model_name].append({
                        'hour_sort': record.hour_sort,
                        'a': record.a,
                        'b': record.b,
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
                elif model_name in ['TripleCaliente', 'TripleCaracas', 'TripleZulia', 'TripleZamorano', 'TripleChance', 'TripleTachira']:
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
