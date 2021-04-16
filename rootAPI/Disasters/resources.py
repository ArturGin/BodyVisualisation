from import_export import resources
from .models import Disasters


class DisasterResource(resources.ModelResource):
    class Meta:
        model = Disasters
