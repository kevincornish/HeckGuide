from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Count

from allies.models import Ally, HistoricalAlly, Clan

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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        object_list = (Ally.objects.all())
        data['clans'] = object_list.distinct('group_tag').exclude(group_tag__isnull=True)
        return data

class NameChangeListView(LoginRequiredMixin, ListView):
    model = HistoricalAlly
    paginate_by = 20
    context_object_name = 'historicalallies'

    def get_queryset(self):
        try:
            username = self.request.GET.get('username')
            object_list = HistoricalAlly.objects.all().values("username", "user_id", "group_tag").order_by('username').distinct()
            if username:
                user_list = object_list.filter(username__iexact=username)
                user_id = user_list[0]["user_id"]
                object_list = user_list.filter(user_id=user_id)
        except IndexError:
            pass
        return object_list

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data

class ClanListView(ListView):
    model = Clan
    paginate_by = 20
    context_object_name = 'clans'

    def get_queryset(self):
        realm = self.request.GET.get('realm')
        object_list = (Clan.objects.all().order_by('-id'))
        if realm:
            object_list = object_list.filter(region__exact=realm)
            
        return object_list

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data