from rest_framework.permissions import (
    BasePermission
)


class IsClient(BasePermission):

    def has_permission(
        self,
        request,
        view
    ):

        return (
            request.user.is_authenticated
            and
            request.user.role == 'CLIENT'
        )


class IsEmploye(BasePermission):

    def has_permission(
        self,
        request,
        view
    ):

        return (
            request.user.is_authenticated
            and
            request.user.role == 'EMPLOYE'
        )


class IsRetail(BasePermission):

    def has_permission(
        self,
        request,
        view
    ):

        return (
            request.user.is_authenticated
            and
            request.user.role == 'RETAIL'
        )


class IsRisque(BasePermission):

    def has_permission(
        self,
        request,
        view
    ):

        return (
            request.user.is_authenticated
            and
            request.user.role == 'RISQUE'
        )


class IsComite(BasePermission):

    def has_permission(
        self,
        request,
        view
    ):

        return (
            request.user.is_authenticated
            and
            request.user.role == 'COMITE'
        )


class IsAdmin(BasePermission):

    def has_permission(
        self,
        request,
        view
    ):

        return (
            request.user.is_authenticated
            and
            request.user.role == 'ADMIN'
        )


class IsBankStaff(BasePermission):

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

                'RETAIL',

                'RISQUE',

                'COMITE',

                'ADMIN'
            ]
        )


class CanManageScoring(BasePermission):

    def has_permission(
        self,
        request,
        view
    ):

        return (
            request.user.is_authenticated
            and
            request.user.role in [

                'RISQUE',

                'ADMIN'
            ]
        )