from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required

from .forms import TokenCalculatorForm, BrewCalculatorForm, TroopMightForm, RallyCalculatorForm

def Index(request):
    return render(request, "index.html")

def Timer(request):
    return render(request, "timer.html")

@login_required
def Account(request):
    return render(request, "account.html")

def TokenCalculatorView(request):
  if request.method == 'POST':
    form = TokenCalculatorForm(request.POST)
    if form.is_valid():   
        token1 = form.cleaned_data['token1'] * 500
        token2 = form.cleaned_data['token2'] * 1000
        token3 = form.cleaned_data['token3'] * 2500
        token4 = form.cleaned_data['token4'] * 5000
        token5 = form.cleaned_data['token5'] * 10000
        token6 = form.cleaned_data['token6'] * 25000
        token7 = form.cleaned_data['token7'] * 50000
        token8 = form.cleaned_data['token8'] * 100000
        token9 = form.cleaned_data['token9'] * 250000
        token10 = form.cleaned_data['token10'] * 500000
        token11 = form.cleaned_data['token11'] * 1000000
        total = token1+token2+token3+token4+token5+token6+token7+token8+token9+token10+token11
    return render(request, 'calculators/TokenCalculator.html', {'form': form, 'token1': token1, 'token2': token2, 'token3': token3, 'token4': token4, 'token5': token5, 'token6': token6, 'token7': token7, 'token8': token8, 'token9': token9, 'token10': token10, 'token11': token11, 'total': total})
  else:
    form = TokenCalculatorForm()       
    return render(request, 'calculators/TokenCalculator.html', {'form': form})

def BrewCalculatorView(request):
  if request.method == 'POST':
    form = BrewCalculatorForm(request.POST)
    if form.is_valid():
        token1 = form.cleaned_data['token1'] * 10
        token2 = form.cleaned_data['token2'] * 25
        token3 = form.cleaned_data['token3'] * 50
        token4 = form.cleaned_data['token4'] * 100
        token5 = form.cleaned_data['token5'] * 250
        total = token1+token2+token3+token4+token5
    return render(request, 'calculators/BrewCalculator.html', {'form': form, 'token1': token1, 'token2': token2, 'token3': token3, 'token4': token4, 'token5': token5, 'total': total})
  else:
    form = BrewCalculatorForm()       
    return render(request, 'calculators/BrewCalculator.html', {'form': form})

def TroopMightView(request):
  if request.method == 'POST':
    form = TroopMightForm(request.POST)
    if form.is_valid():
        troopmight = 150
        might = form.cleaned_data['might']
        trainkill = form.cleaned_data['trainkill']
        troops = form.cleaned_data['troops']
        if trainkill == "2":
          newmight = might - troops * troopmight
          troopstag = "Killed"
          mighttag = "Lost"
        elif trainkill == "1":
          newmight = troops * troopmight + might
          troopstag = "Trained"
          mighttag = "Gained"
        if newmight < 0:
            newmight = 0
        mightdiff = newmight - might
    return render(request, 'calculators/TroopMight.html', {'form': form, 'mighttag': mighttag, 'mightdiff': mightdiff, 'troopstag': troopstag, 'might': might, 'trainkill': trainkill, 'troops': troops, 'newmight': newmight})
  else:
    form = TroopMightForm()       
    return render(request, 'calculators/TroopMight.html', {'form': form})

def RallyCalculatorView(request):
  if request.method == 'POST':
    form = RallyCalculatorForm(request.POST)
    if form.is_valid():
        bossstrength = form.cleaned_data['bossstrength']
        attackpower = form.cleaned_data['attackpower']
        marchcap = form.cleaned_data['marchcap']
        try:
          joiners = int(bossstrength / (attackpower / marchcap)- marchcap)
          totalrally = int(bossstrength /(attackpower / marchcap))
        except ZeroDivisionError:
          joiners = 0
          totalrally = 0
    return render(request, 'calculators/RallyCalculator.html', {'form': form, 'joiners': joiners, 'totalrally': totalrally})
  else:
    form = RallyCalculatorForm()
    return render(request, 'calculators/RallyCalculator.html', {'form': form})
