from rest_framework.permissions import BasePermission


class IsEmployeOrAdmin(
    BasePermission
):

    def has_permission(
        self,
        request,
        view
    ):

        return (
            request.user.is_authenticated
            and
            request.user.role in [
                'EMPLOYE',
                'ADMIN'
            ]
        )