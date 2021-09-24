from django.db import models

class RealmChat(models.Model):
    id = models.IntegerField(primary_key=True, db_index=True)
    username = models.CharField(max_length=255, null=True)
    message = models.CharField(max_length=255, null=True)
    timestamp = models.IntegerField(null=True)
    user_id = models.IntegerField(null=True)
    user_avatar_id = models.IntegerField(null=True)
    user_avatar_type = models.IntegerField(null=True)
    type = models.IntegerField(null=True)
    region = models.IntegerField(null=True)

class RealmList(models.Model):
    id = models.IntegerField(primary_key=True, db_index=True)
    spawned_user_count = models.IntegerField(null=True)
    maximum_transfer_power = models.IntegerField(null=True)
    maximum_transfer_townhall_level = models.IntegerField(null=True)
    name = models.CharField(max_length=255, null=True)
    subname = models.CharField(max_length=255, null=True)
    pvp_rating = models.CharField(max_length=255, null=True)