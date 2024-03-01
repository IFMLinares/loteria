from django.urls import path
from core.views import (
    LotteryView,

    # Vista de Listas 

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

    # Vistas de Resultados por grupo:
    AddGroupResultA,
    AddGroupResultB,
    AddGroupResultC,
    AddGroupResultD,
    AddGroupResultE,
)

app_name = "core"
urlpatterns = [
    path("", view=LotteryView.as_view(), name="lottery"),
    # URLS De vistas

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

    # URLS De Resultados por grupo
    path("administrador/add_group_a", view=AddGroupResultA.as_view(), name="group_a"),
    path("administrador/add_group_b", view=AddGroupResultB.as_view(), name="group_b"),
    path("administrador/add_group_c", view=AddGroupResultC.as_view(), name="group_c"),
    path("administrador/add_group_d", view=AddGroupResultD.as_view(), name="group_d"),
    path("administrador/add_group_e", view=AddGroupResultE.as_view(), name="group_e"),
]
