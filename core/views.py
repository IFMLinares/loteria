from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class LotteryView(View):
    def get(self, request):
        # Lógica de tu vista aquí
        return render(request, 'lotoview/index.html')