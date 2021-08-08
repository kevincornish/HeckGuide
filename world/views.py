from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from world.models import WorldSegments

class WorldListView(LoginRequiredMixin, ListView):
    model = WorldSegments
    paginate_by = 20
    context_object_name = 'worldsegments'

    def get_queryset(self):
        object_list = (
            WorldSegments.objects.all()
        )
        return object_list