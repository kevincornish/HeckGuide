from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from allies.views import AllyListView, NameChangeListView, ClanListView, ClanDetailView
from world.views import WorldListView
from poll.views import RealmChatView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    path('allies/', AllyListView.as_view(template_name="allies/allies.html"), name='allies'),
    path('clans/', ClanListView.as_view(template_name="allies/clans.html"), name='clans'),
    path('clans/<tag>/', ClanDetailView.as_view(), name='clandetail'),
    path('name-changes/', NameChangeListView.as_view(template_name="allies/name_changes.html"), name='namechanges'),
    path('world/', WorldListView.as_view(template_name="world/world.html"), name='world'),
    path('realm-chat/', RealmChatView.as_view(template_name="poll/realm_chat.html"), name='realmchat'),
    path('api-auth/', include('rest.urls')),
    path('invitations/', include('invitations.urls', namespace='invitations')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns