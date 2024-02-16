from datetime import time
from collections import defaultdict
from django.shortcuts import render
from django.views.generic import View
from django.utils import timezone
from .models import *
# Create your views here.

class LotteryView(View):
    def get(self, request):
        # # Obtén la fecha actual
        # today = timezone.now().date()

        # # Realiza la consulta para obtener todos los resultados de hoy
        # today_results = ChanceAnimalitos.objects.filter(date_sort=today)

        # # Crea un diccionario con todos los horarios posibles
        # results_dict = defaultdict(lambda: "-----")
        # for hour, _ in HOUR_CHOICES:
        #     results_dict[hour]

        # # Llena el diccionario con los resultados de hoy
        # for result in today_results:
        #     results_dict[result.hour_sort] = result.get_animalito_display()

        # # Pasa los resultados al contexto de la plantilla
        # context = {'results': dict(results_dict)}

        return render(request, 'lotoview/index.html')