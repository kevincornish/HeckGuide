from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from poll.models import RealmChat


class RealmChatView(ListView):

    model = RealmChat
    paginate_by = 20
    context_object_name = 'realmchat'

    def get_queryset(self):
        player = self.request.GET.get('player')
        user_id = self.request.GET.get('user_id')
        realm = self.request.GET.get('realm')
        object_list = (
            RealmChat.objects.all().order_by('-timestamp').exclude(message__isnull=True)
        )
        if player:
            object_list = object_list.filter(username__icontains=player)
        if realm:
            object_list = object_list.filter(region__iexact=realm)
        if user_id:
            object_list = object_list.filter(user_id__exact=user_id)
        return object_list

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        object_list = (RealmChat.objects.all().exclude(region__isnull=True))
        data['realms'] = object_list.distinct('region')
        return data
