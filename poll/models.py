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