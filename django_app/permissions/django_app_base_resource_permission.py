from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import BasePermission


class DjangoAppBaseResourcePermission(BasePermission):
    message = "You do not have enough permissions to access this resource"

    permission_map = {
        "GET": "{app_label}.view_{resource_name}",
        "POST": "{app_label}.add_{resource_name}",
        "PUT": "{app_label}.change_{resource_name}",
        "PATCH": "{app_label}.change_{resource_name}",
        "DELETE": "{app_label}.delete_{resource_name}",
    }

    def get_permission(self, request_method, app_label, resource_name):

        if request_method not in self.permission_map:
            raise MethodNotAllowed(request_method)

        permission = self.permission_map.get(
            request_method
        ).format(
            app_label=app_label,
            resource_name=resource_name
        )

        return permission

    def has_permission(self, request, view):
        permission = self.get_permission(
            request_method=request.method,
            app_label=view.app_label,
            resource_name=view.resource_name
        )

        return request.user.has_perm(permission)
