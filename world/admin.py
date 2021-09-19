from django.contrib import admin
from .models import WorldSegments

class WorldSegmentsAdmin(admin.ModelAdmin):
  list_display = ('description', 'name', 'owner_group_name', 'owner_username', 'world_id', 'created', 'last_modified')
  search_fields = ['owner_username']

admin.site.register(WorldSegments, WorldSegmentsAdmin)