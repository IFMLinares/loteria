from datetime import time
from collections import defaultdict
from django.shortcuts import render
from django.views.generic import View
from django.utils import timezone
from .models import *
# Create your views here.

class LotteryView(View):
    def get(self, request):
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
            ]  # Agrega los otros modelos a esta lista

        for model in models:
            model_name = model.__name__
            today = timezone.now().date()
            hours = [choice[0] for choice in model._meta.get_field('hour_sort').choices]
            records = model.objects.filter(date_sort=today)
            records_dict = {record.hour_sort: record for record in records}

            context[model_name] = []
            for hour in hours:
                if hour in records_dict:
                    record = records_dict[hour]
                    context[model_name].append({
                        'hour_sort': record.hour_sort,
                        'animalito': record.animalito,
                        'animalito_name': dict(model._meta.get_field('animalito').choices)[record.animalito],
                        'image_path': record.get_image_path(),
                    })
                else:
                    context[model_name].append({
                        'hour_sort': hour,
                        'animalito': '----------',
                        'animalito_name': '----------',
                        'image_path': '----------',
                    })
        print(context)
        return render(request, 'lotoview/index.html', context)