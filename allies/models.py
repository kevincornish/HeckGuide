import uuid

from django.db import models

class BaseAlly(models.Model):
    username = models.CharField(max_length=255)
    avatar_type = models.IntegerField(null=True)
    avatar_id = models.IntegerField(null=True)
    last_shard_transfer = models.IntegerField(null=True)
    home_world_id = models.IntegerField(null=True)
    group_tag = models.CharField(max_length=255, null=True)
    group_id = models.BigIntegerField(null=True)
    power = models.IntegerField(null=True)
    troop_kills = models.BigIntegerField(null=True)
    active = models.BooleanField(null=True)
    cost = models.BigIntegerField(null=True)
    previous_cost = models.BigIntegerField(null=True)
    biome1_attack_multiplier = models.IntegerField(null=True)
    biome2_attack_multiplier = models.IntegerField(null=True)
    biome3_attack_multiplier = models.IntegerField(null=True)
    biome4_attack_multiplier = models.IntegerField(null=True)
    biome5_attack_multiplier = models.IntegerField(null=True)
    biome6_attack_multiplier = models.IntegerField(null=True)
    biome7_attack_multiplier = models.IntegerField(null=True)
    biome8_attack_multiplier = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    class Meta:
        abstract = True

class Ally(BaseAlly):
    user_id = models.IntegerField(primary_key=True)
    owner = models.ForeignKey('self', null=True, related_name='owned_allies', on_delete=models.RESTRICT)

    def historical_records(self):
        return HistoricalAlly.objects.filter(user_id=self.user_id)

class HistoricalAlly(BaseAlly):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.IntegerField(db_index=True)
    owner = models.ForeignKey(Ally, null=True, related_name='owned_historical_allies', on_delete=models.RESTRICT)
