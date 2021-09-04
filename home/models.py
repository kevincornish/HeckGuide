from django.db import models
from django.contrib.auth.models import User

class Webhooks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='webhooks')
    item = models.CharField(max_length=500)
    realm = models.IntegerField(default=0)
    hookurl = models.URLField(max_length = 200)