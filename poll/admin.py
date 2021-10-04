from django.contrib import admin
from .models import ClanChat

class ClanChatAdmin(admin.ModelAdmin):
  list_display = ('mail_id', 'username', 'message', 'realm')

admin.site.register(ClanChat, ClanChatAdmin)