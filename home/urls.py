from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index, name='homepage'),
    path('Token-Calculator/', views.TokenCalculatorView, name='TokenCalculator'),
    path('Brew-Calculator/', views.BrewCalculatorView, name='BrewCalculator'),
    path('Troop-Might/', views.TroopMightView, name='TroopMight'),
    path('Rally-Calculator/', views.RallyCalculatorView, name='RallyCalculator'),
]
