from django.contrib import admin
from .models import Webhooks

class WebhooksAdmin(admin.ModelAdmin):
    list_display = ('user','item', 'hookurl')
    fields = ('user','item', 'hookurl')
  
admin.site.register(Webhooks, WebhooksAdmin)