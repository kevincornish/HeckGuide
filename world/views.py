from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from world.models import WorldSegments

class WorldListView(LoginRequiredMixin, ListView):
    model = WorldSegments
    paginate_by = 20
    context_object_name = 'worldsegments'

    def get_queryset(self):
        player = self.request.GET.get('player')
        clan = self.request.GET.get('clan')
        object_list = (
            WorldSegments.objects.all().order_by('-x')
        )
        if player:
            object_list = object_list.filter(owner_username__iexact=player)
        if clan:
            object_list = object_list.filter(owner_group_name__iexact=clan)
        return object_list

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        object_list = (WorldSegments.objects.all())
        data['clans'] = object_list.distinct('owner_group_name').exclude(owner_group_name__isnull=True)
        return data