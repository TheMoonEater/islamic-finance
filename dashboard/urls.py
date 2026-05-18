from django.urls import path

from .views import (
    DashboardStatsView,
    WorkflowStatsView
)

from .views import (
    DashboardStatsView
)

urlpatterns = [

    path(
        'dashboard/stats/',
        DashboardStatsView.as_view()
    ),
    path(
    'dashboard/workflow-stats/',
    WorkflowStatsView.as_view()
),
]

