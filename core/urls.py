from django.urls import path
from core.views import (
    LotteryView,

    # Vista del Administrador

    # Index
    IndexView,

    # Listados Animalitos
    AdminChanceAnimalitos,
    AdminGranjaPlus,
    AdminLaGranjita,
    AdminLaRicachona,
    AdminLottoActivo,
    AdminLottoActivoInterRD,
    AdminLottoRey,
    AdminSelvaPlus,
    AdminGuacharoActivo,
    AdminGranjaMillonaria,
    AdminGranjazo,

    # Listados Loterias
    AdminTripleCaliente,
    AdminTripleCaracas,
    AdminTripleZulia,
    AdminTripleZamorano,
    AdminTripleChance,
    AdminTripleChance,
    AdminTrioActivo,
    AdminRicachona,

    # Vistas de Resultados por grupo:
    AddGroupResultA,
    AddGroupResultB,
    AddGroupResultC,
    AddGroupResultD,
    AddGroupResultE,

    AddLoteryGroupResultA,
    AddLoteryGroupResultB,
    AddLoteryGroupResultC,
    AddLoteryGroupResultD,
    AddLoteryGroupResultE,
    AddLoteryGroupResultF,
    AddLoteryGroupResultG,
)

app_name = "core"
urlpatterns = [
    path("", view=LotteryView.as_view(), name="lottery"),
    # URLS De vistas

    path("administrador/", view=IndexView.as_view(), name="index"),

    # Listados de Animalitos
    path("administrador/chanceAnimalitos", view=AdminChanceAnimalitos.as_view(), name="chanceAnimalitos"),
    path("administrador/granjaPlus", view=AdminGranjaPlus.as_view(), name="granjaPlus"),
    path("administrador/laGranjita", view=AdminLaGranjita.as_view(), name="laGranjita"),
    path("administrador/laRicachona", view=AdminLaRicachona.as_view(), name="laRicachona"),
    path("administrador/lottoActivo", view=AdminLottoActivo.as_view(), name="lottoActivo"),
    path("administrador/lottoActivoInterRD", view=AdminLottoActivoInterRD.as_view(), name="lottoActivoInterRD"),
    path("administrador/lottoRey", view=AdminLottoRey.as_view(), name="lottoRey"),
    path("administrador/selvaPlus", view=AdminSelvaPlus.as_view(), name="selvaPlus"),
    path("administrador/guacharoActivo", view=AdminGuacharoActivo.as_view(), name="guacharoActivo"),
    path("administrador/granjaMillonaria", view=AdminGranjaMillonaria.as_view(), name="granjaMillonaria"),
    path("administrador/granjazo", view=AdminGranjazo.as_view(), name="granjazo"),
    path("administrador/granjazo", view=AdminGranjazo.as_view(), name="granjazo"),

    # URLS LISTADOS DE LOTERIAS
    path("administrador/triple_caliente", view=AdminTripleCaliente.as_view(), name="triple_caliente"),
    path("administrador/triple_caracas", view=AdminTripleCaracas.as_view(), name="triple_caracas"),
    path("administrador/triple_zulia", view=AdminTripleZulia.as_view(), name="triple_zulia"),
    path("administrador/triple_zamorano", view=AdminTripleZamorano.as_view(), name="triple_zamorano"),
    path("administrador/triple_chance", view=AdminTripleChance.as_view(), name="triple_chance"),
    path("administrador/triple_tachira", view=AdminTripleChance.as_view(), name="triple_tachira"),
    path("administrador/trio_activo", view=AdminTrioActivo.as_view(), name="trio_activo"),
    path("administrador/ricachona", view=AdminRicachona.as_view(), name="ricachona"),


    # URLS De Resultados por grupo
    path("administrador/add_group_a", view=AddGroupResultA.as_view(), name="group_a"),
    path("administrador/add_group_b", view=AddGroupResultB.as_view(), name="group_b"),
    path("administrador/add_group_c", view=AddGroupResultC.as_view(), name="group_c"),
    path("administrador/add_group_d", view=AddGroupResultD.as_view(), name="group_d"),
    path("administrador/add_group_e", view=AddGroupResultE.as_view(), name="group_e"),


    path("administrador/add_lotery_group_a", view=AddLoteryGroupResultA.as_view(), name="lotery_group_a"),
    path("administrador/add_lotery_group_b", view=AddLoteryGroupResultB.as_view(), name="lotery_group_b"),
    path("administrador/add_lotery_group_c", view=AddLoteryGroupResultC.as_view(), name="lotery_group_c"),
    path("administrador/add_lotery_group_d", view=AddLoteryGroupResultD.as_view(), name="lotery_group_d"),
    path("administrador/add_lotery_group_e", view=AddLoteryGroupResultE.as_view(), name="lotery_group_e"),
    path("administrador/add_lotery_group_f", view=AddLoteryGroupResultF.as_view(), name="lotery_group_f"),
    path("administrador/add_lotery_group_g", view=AddLoteryGroupResultG.as_view(), name="lotery_group_g"),
]
