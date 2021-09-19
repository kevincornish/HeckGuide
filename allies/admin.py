from django.contrib import admin
from .models import Ally, HistoricalAlly

class AllyAdmin(admin.ModelAdmin):
  list_display = ('username', 'created', 'last_modified')

class HistoricalAllyAdmin(admin.ModelAdmin):
  list_display = ('username', 'user_id', 'created', 'last_modified')
  search_fields = ['username', 'user_id']

admin.site.register(Ally, AllyAdmin)
admin.site.register(HistoricalAlly, HistoricalAllyAdmin)