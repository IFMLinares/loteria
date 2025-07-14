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
    AdminTerminalito,
    AdminFruitaGana,
    AdminGuacharito,

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
    AddGroupResultF,

    AddLoteryGroupResultA,
    AddLoteryGroupResultB,
    AddLoteryGroupResultC,
    AddLoteryGroupResultD,
    AddLoteryGroupResultE,
    AddLoteryGroupResultF,
    AddLoteryGroupResultG,

    ChanceAnimalitosView,
    GranjaPlusView,
    LaGranjitaView,
    LaRicachonaView,
    LottoActivoView,
    LottoActivoInterRDView,
    LottoReyView,
    SelvaPlusView,
    GuacharoActivoView,
    GranjaMillonariaView,
    GranjazoView,
    TerminalitoView,
    FruitaGanaView,
    GuacharitoView,

    TripleCalienteView,
    TripleCaracasView,
    TripleZuliaView,
    TripleZamoranoView,
    TripleChanceView,
    TripleTachiraView,
    TrioActivoView,
    RicachonaView,

    # USUARIOS
    RegisterUserView,
    UserListView,
    VideosDelDiaListView,
    UploadVideo,
    VideoModelTodayListView,

    # AJAX VIEW
    # DeleteObjectView,
    ajax_delete_view,
    upload_video,
    delete_video,
    upload_video_today_page,
    update_time_pages,
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
    path("administrador/terminalito", view=AdminTerminalito.as_view(), name="terminalito"),
    path("administrador/fruitaGana", view=AdminFruitaGana.as_view(), name="fruitaGana"),
    path("administrador/guacharito", view=AdminGuacharito.as_view(), name="guacharito"),

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
    path("administrador/add_group_f", view=AddGroupResultF.as_view(), name="group_f"),


    path("administrador/add_lotery_group_a", view=AddLoteryGroupResultA.as_view(), name="lotery_group_a"),
    path("administrador/add_lotery_group_b", view=AddLoteryGroupResultB.as_view(), name="lotery_group_b"),
    path("administrador/add_lotery_group_c", view=AddLoteryGroupResultC.as_view(), name="lotery_group_c"),
    path("administrador/add_lotery_group_d", view=AddLoteryGroupResultD.as_view(), name="lotery_group_d"),
    path("administrador/add_lotery_group_e", view=AddLoteryGroupResultE.as_view(), name="lotery_group_e"),
    path("administrador/add_lotery_group_f", view=AddLoteryGroupResultF.as_view(), name="lotery_group_f"),
    path("administrador/add_lotery_group_g", view=AddLoteryGroupResultG.as_view(), name="lotery_group_g"),
    
    path("administrador/chance_animalitos_add", view=ChanceAnimalitosView.as_view(), name="chance_animalitos_add"),
    path("administrador/granja_plus_add", view=GranjaPlusView.as_view(), name="granja_plus_add"),
    path("administrador/la_granjita_add", view=LaGranjitaView.as_view(), name="la_granjita_add"),
    path("administrador/ricachona_add", view=LaRicachonaView.as_view(), name="ricachona_add"),
    path("administrador/lotto_activo_add", view=LottoActivoView.as_view(), name="lotto_activo_add"),
    path("administrador/lotto_Activo_inter_rd_add", view=LottoActivoInterRDView.as_view(), name="lotto_Activo_inter_rd_add"),
    path("administrador/lotto_rey_add", view=LottoReyView.as_view(), name="lotto_rey_add"),
    path("administrador/selva_plus_add", view=SelvaPlusView.as_view(), name="selva_plus_add"),
    path("administrador/guacharo_activo_add", view=GuacharoActivoView.as_view(), name="guacharo_activo_add"),
    path("administrador/granja_millonaria_add", view=GranjaMillonariaView.as_view(), name="granja_millonaria_add"),
    path("administrador/granjazo_add", view=GranjazoView.as_view(), name="granjazo_add"),
    path("administrador/terminalito_add", view=TerminalitoView.as_view(), name="terminalito_add"),
    path("administrador/fruitaGana_add", view=FruitaGanaView.as_view(), name="fruitaGana_add"),
    path("administrador/guacharito_add", view=GuacharitoView.as_view(), name="guacharito_add"),


    path("administrador/triple_caliente_add", view=TripleCalienteView.as_view(), name="triple_caliente_add"),
    path("administrador/triple_caracas_add", view=TripleCaracasView.as_view(), name="triple_caracas_add"),
    path("administrador/triple_zulia_add", view=TripleZuliaView.as_view(), name="triple_zulia_add"),
    path("administrador/triple_zamorano_add", view=TripleZamoranoView.as_view(), name="triple_zamorano_add"),
    path("administrador/triple_chance_add", view=TripleChanceView.as_view(), name="triple_chance_add"),
    path("administrador/triple_tachira_add", view=TripleTachiraView.as_view(), name="triple_tachira_add"),
    path("administrador/trio_activo_add", view=TrioActivoView.as_view(), name="trio_activo_add"),
    path("administrador/la_ricachona_add", view=RicachonaView.as_view(), name="la_ricachona_add"),
    path("administrador/videos/upload", view=UploadVideo.as_view(), name="videos_upload"),
    path("administrador/videos/list", view=VideoModelTodayListView.as_view(), name="videos_list"),

    

    # USUARIOS
    path("administrador/users/register", view=RegisterUserView.as_view(), name="user_register"),
    path('users/', UserListView.as_view(), name='user_list'),
    path('videos/today/', VideosDelDiaListView.as_view(), name='videos-del-dia'),

    # AJAX VIEW
    
    # path("administrador/ajax/delete_view", view=DeleteObjectView.as_view(), name="ajax_delete_view"),
    path('administrador/ajax/delete_view/', ajax_delete_view, name='ajax_delete_view'),
    path('administrador/ajax/upload_video/', upload_video, name='upload_video'),
    path('administrador/ajax/upload_video_today_page/', upload_video_today_page, name='upload_video_today_page'),
    path('administrador/ajax/delete_video/', delete_video, name='delete_video'),
    path('administrador/ajax/update_time/', update_time_pages, name='update_time'),
]
