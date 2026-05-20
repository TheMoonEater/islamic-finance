from rest_framework.views import APIView
from rest_framework.response import Response

from .services import (
    demandes_by_status
)

from rest_framework.permissions import (
    IsAuthenticated
)

from users.permissions import (
    IsBankStaff,
)

from .services import (
    get_dashboard_stats
)


class DashboardStatsView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsBankStaff,
    ]

    def get(self, request):

        data = get_dashboard_stats()

        return Response(data)
    

class WorkflowStatsView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsBankStaff
    ]

    def get(self, request):

        data = demandes_by_status()

        return Response(data)


# No module-level permission_classes required; views define their own