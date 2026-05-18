from django.urls import path
from .views import CalculateScoringView

urlpatterns = [
    path(
        'scoring/calculate/',
        CalculateScoringView.as_view()
    ),
]