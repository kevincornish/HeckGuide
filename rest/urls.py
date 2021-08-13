from django.urls import include, path
from rest_framework import routers
from rest import views

router = routers.DefaultRouter()
router.register(r'allies', views.AllyViewSet)
router.register(r'world', views.MapViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]