from django.urls import path

from .views import (
    ScoringConfigView
)

urlpatterns = [

    path(
        "",
        ScoringConfigView.as_view()
    ),

]