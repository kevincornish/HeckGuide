from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index, name='homepage'),
    path('Timer/', views.Timer, name='timer'),
    path('Prices/', views.Prices, name='prices'),
    path('Account/', views.Account, name='account'),
    path('Account/Discord', views.AccountDiscord, name='account_discord'),
    path('Account/Discord/Delete/<int:id>', views.delete_webhook, name='account_discord_delete'),
    path('Token-Calculator/', views.TokenCalculatorView, name='TokenCalculator'),
    path('Brew-Calculator/', views.BrewCalculatorView, name='BrewCalculator'),
    path('Troop-Might/', views.TroopMightView, name='TroopMight'),
    path('Rally-Calculator/', views.RallyCalculatorView, name='RallyCalculator'),
    path('Mastery-Calculator/', views.MasteryCalculatorView, name='MasteryCalculator'),
    path('AllyStat-Calculator/', views.AllyStatView, name='AllyStatCalculator'),
]