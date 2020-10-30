from rest_framework.permissions import BasePermission

from p7.models import is_professional, is_company


class P7Permission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class StaffPermission(BasePermission):
    def has_permission(self, request, view):
        required_privilege = view.required_privilege
        return bool(request.user and request.user.is_authenticated and request.user.is_staff
                    and request.user.has_perm(required_privilege))


class ProfessionalPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and is_professional(request.user))


class CompanyPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and is_company(request.user))


