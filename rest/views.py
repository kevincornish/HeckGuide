from allies.models import Ally, HistoricalAlly
from world.models import WorldSegments
from rest_framework import viewsets
from rest_framework import permissions
from rest.serializers import AllySerializer, MapSerializer, HistoricalAllySerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
	
class AllyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows allies to be viewed.
    """
    queryset = Ally.objects.all().exclude(cost__isnull=True).order_by('-cost')
    serializer_class = AllySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['cost']
    search_fields = ['=owner__username', '=cost']

class HistoricalAllySerializerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows historical allies to be viewed.
    """
    queryset = HistoricalAlly.objects.all().values("username", "user_id", "group_tag").order_by('username').distinct()
    serializer_class = HistoricalAllySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['=username']
	
class MapViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows allies to be viewed.
    """
    queryset = WorldSegments.objects.all().order_by('-x')
    serializer_class = MapSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'owner_username', 'owner_group_name','world_id']
    search_fields = ['=name', '=owner_username', '=owner_group_name','=world_id']