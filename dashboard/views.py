from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsBankStaff

from .services import (
    dashboard_charts,
    get_dashboard_stats,
    demandes_by_status
)


class DashboardStatsView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsBankStaff,
    ]

    def get(self, request):

        return Response(
            dashboard_charts()
        )


class WorkflowStatsView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsBankStaff,
    ]

    def get(self, request):

        return Response(
            demandes_by_status()
        )