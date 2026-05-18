from django.urls import path
from .views import CreateSimulationView

urlpatterns = [
    path(
        'simulation/create/',
        CreateSimulationView.as_view()
    ),
]