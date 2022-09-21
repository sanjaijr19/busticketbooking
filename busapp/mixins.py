from django.core.exceptions import PermissionDenied
class CheckPremiumGroupMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.groups.filter(name = "driver").exists():
            #return True
            return super().dispatch(request, *args, **kwargs)

        else:
            raise