from django.core.management.base import BaseCommand
from datetime import timedelta
from django.utils import timezone

from ...models import (
    ChanceAnimalitos,
    FruitaGana,
    GranjaMillonaria,
    GranjaPlus,
    Granjazo,
    GuacharoActivo,
    LaGranjita,
    LaRicachona,
    LottoActivo,
    LottoActivoInterRD,
    LottoRey,
    Ricachona,
    SelvaPlus,
    Terminalito,
    TrioActivo,
    TripleCaliente,
    TripleCaracas,
    TripleChance,
    TripleTachira,
    TripleZamorano,
    TripleZulia
)

class Command(BaseCommand):
    help = 'eliminar_registros_antiguos'

    def handle(self, *args, **kwargs):
        modelos = [
            ChanceAnimalitos,
            FruitaGana,
            GranjaMillonaria,
            GranjaPlus,
            Granjazo,
            GuacharoActivo,
            LaGranjita,
            LaRicachona,
            LottoActivo,
            LottoActivoInterRD,
            LottoRey,
            Ricachona,
            SelvaPlus,
            Terminalito,
            TrioActivo,
            TripleCaliente,
            TripleCaracas,
            TripleChance,
            TripleTachira,
            TripleZamorano,
            TripleZulia
        ]

        for modelo in modelos:
            modelo.eliminar_registros_antiguos()
            self.stdout.write(self.style.SUCCESS(f'Registros antiguos eliminados para {modelo.__name__}'))