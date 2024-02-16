from django.urls import path
from core.views import (
    LotteryView,
)

app_name = "core"
urlpatterns = [
    path("", view=LotteryView.as_view(), name="lottery"),
]
