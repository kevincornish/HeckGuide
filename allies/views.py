from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Count

from allies.models import Ally

class AllyListView(LoginRequiredMixin, ListView):
    model = Ally
    paginate_by = 20
    context_object_name = 'allies'

    def get_queryset(self):
        owned_by = self.request.GET.get('current_owner')
        cost = self.request.GET.get('cost')
        clan = self.request.GET.get('clan')
        object_list = (
            Ally.objects.all().order_by('-cost').exclude(cost__isnull=True)
            .annotate(Count('owned_allies'))
        )
        if owned_by:
            object_list = object_list.filter(owner__username__iexact=owned_by)
        if cost:
            object_list = object_list.filter(cost__lte=cost, cost__gte=0)
        if clan:
            object_list = object_list.filter(group_tag=clan)
        return object_list
