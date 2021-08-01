from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.Index, name='homepage'),
    path('Token-Calculator/', views.TokenCalculator.as_view(), name='TokenCalculator'),
    path('Brew-Calculator/', views.BrewCalculator.as_view(), name='BrewCalculator'),
]