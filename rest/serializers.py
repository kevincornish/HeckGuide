from allies.models import Ally
from world.models import WorldSegments
from rest_framework import serializers
		
class AllySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ally
        fields = ['username', 'group_tag' , 'cost','biome3_attack_multiplier','biome4_attack_multiplier','biome5_attack_multiplier', 'last_modified']

		
class MapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorldSegments
        fields = ['name', 'owner_group_name', 'owner_username', 'x', 'y', 'world_id', 'last_modified']