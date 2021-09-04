from django.contrib import admin
from .models import Webhooks

class WebhooksAdmin(admin.ModelAdmin):
    list_display = ('user','item', 'hookurl','realm')
    fields = ('user','item', 'hookurl','realm')
  
admin.site.register(Webhooks, WebhooksAdmin)