from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .forms import TokenCalculatorForm, BrewCalculatorForm, TroopMightForm, RallyCalculatorForm, MasteryCalculatorForm, WebhookForm
from .models import Webhooks
from world.models import WorldSegments

def Index(request):
    return render(request, "index.html")

def Timer(request):
    return render(request, "timer.html")

def Prices(request):
    return render(request, "prices.html", {'prices_1': settings.PRICES_1, 'prices_2': settings.PRICES_2, 'prices_3': settings.PRICES_3, 
                                            'prices_4': settings.PRICES_4, 'prices_5': settings.PRICES_5})

@login_required
def Account(request):
  return render(request, 'account.html')

@login_required
def AccountDiscord(request):

    webhooks = Webhooks.objects.all().filter(user=request.user)
    items = WorldSegments.objects.distinct('name').exclude(owner_user_id__isnull=False)
    realms = WorldSegments.objects.distinct('world_id')
    if request.method == 'POST':
        form = WebhookForm(request.POST)
        if form.is_valid():
            Webhooks.objects.create(user=request.user, item=form.cleaned_data.get('item'), realm=form.cleaned_data.get('realm'),
                                   hookurl=form.cleaned_data.get('hookurl'))
            messages.add_message(request, 25 , 'Notification added.')
        else:
            messages.add_message(request, 40, "Notification couldn't be added.")
    else:
        form = WebhookForm()
    return render(request, 'allauth/account/discord.html', {
        'form': form, 'webhooks': webhooks, 'items': items, 'realms': realms
    })

@login_required
def delete_webhook(request, id):
  try:
      query = Webhooks.objects.get(id=id,user=request.user)
      query.delete()
      messages.add_message(request, 25 , 'Notification deleted.')
  except ObjectDoesNotExist:
      messages.add_message(request, 40 , 'Notification failed to be deleted.')
  return redirect('account_discord')

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
    return render(request, 'calculators/TokenCalculator.html', {'form': form, 'token1': token1, 'token2': token2, 'token3': token3, 
    'token4': token4, 'token5': token5, 'token6': token6, 'token7': token7, 'token8': token8, 'token9': token9, 'token10': token10, 'token11': token11, 'total': total})
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
    return render(request, 'calculators/BrewCalculator.html', {'form': form, 'token1': token1, 'token2': token2, 'token3': token3, 
    'token4': token4, 'token5': token5, 'total': total})
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
    return render(request, 'calculators/TroopMight.html', {'form': form, 'mighttag': mighttag, 'mightdiff': mightdiff, 'troopstag': troopstag, 
    'might': might, 'trainkill': trainkill, 'troops': troops, 'newmight': newmight})
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

def MasteryCalculatorView(request):
  if request.method == 'POST':
    form = MasteryCalculatorForm(request.POST)
    if form.is_valid():   
        xpboost = form.cleaned_data['xpboost']
        gatherbonus = form.cleaned_data['gatherbonus']
        attackbonus = form.cleaned_data['attackbonus']
        marchcap = form.cleaned_data['marchcap']
        defcap = form.cleaned_data['defcap']
        attackboost = form.cleaned_data['attackboost']
        defbonus = form.cleaned_data['defbonus']
        statsforallies = form.cleaned_data['statsforallies']
        bonusforallies = form.cleaned_data['bonusforallies']
        marchboost = form.cleaned_data['marchboost']
        abilityboost = form.cleaned_data['abilityboost']
        marchcap2 = form.cleaned_data['marchcap2']

        if xpboost < 11:
          xpgold = 78.88
        elif xpboost == 11:
          xpgold = 77.02
        elif xpboost == 12:
          xpgold = 74.10
        elif xpboost == 13:
          xpgold = 69.80
        elif xpboost == 14:
          xpgold = 64.20
        elif xpboost == 15:
          xpgold = 56.40
        elif xpboost == 16:
          xpgold = 45.90
        elif xpboost == 17:
          xpgold = 33.70
        elif xpboost == 18:
          xpgold = 18.40
        else:
          xpgold = 0

        if gatherbonus < 11:
          gathergold = 78.88
        elif gatherbonus == 11:
          gathergold = 77.02
        elif gatherbonus == 12:
          gathergold = 74.10
        elif gatherbonus == 13:
          gathergold = 69.80
        elif gatherbonus == 14:
          gathergold = 64.20
        elif gatherbonus == 15:
          gathergold = 56.40
        elif gatherbonus == 16:
          gathergold = 45.90
        elif gatherbonus == 17:
          gathergold = 33.70
        elif gatherbonus == 18:
          gathergold = 18.40
        else:
          gathergold = 0

        if attackbonus < 11:
          attackgold = 78.88
        elif attackbonus == 11:
          attackgold = 77.02
        elif attackbonus == 12:
          attackgold = 74.10
        elif attackbonus == 13:
          attackgold = 69.80
        elif attackbonus == 14:
          attackgold = 64.20
        elif attackbonus == 15:
          attackgold = 56.40
        elif attackbonus == 16:
          attackgold = 45.90
        elif attackbonus == 17:
          attackgold = 33.70
        elif attackbonus == 18:
          attackgold = 18.40
        else:
          attackgold = 0

        if marchcap < 11:
          marchgold = 78.88
        elif marchcap == 11:
          marchgold = 77.02
        elif marchcap == 12:
          marchgold = 74.10
        elif marchcap == 13:
          marchgold = 69.80
        elif marchcap == 14:
          marchgold = 64.20
        elif marchcap == 15:
          marchgold = 56.40
        elif marchcap == 16:
          marchgold = 45.90
        elif marchcap == 17:
          marchgold = 33.70
        elif marchcap == 18:
          marchgold = 18.40
        else:
          marchgold = 0

        if defcap < 10:
          defore = 259.94
        elif defcap == 10:
          defore = 252.30
        elif defcap == 11:
          defore = 241.70
        elif defcap == 12:
          defore = 227.60
        elif defcap == 13:
          defore = 209.30
        elif defcap == 14:
          defore = 186.40
        elif defcap == 15:
          defore = 158.60
        elif defcap == 16:
          defore = 125.70
        elif defcap == 17:
          defore = 88.00
        elif defcap == 18:
          defore = 45.90
        else:
          defore = 0

        if attackboost < 10:
          attackfood = 259.94
        elif attackboost == 10:
          attackfood = 252.30
        elif attackboost == 11:
          attackfood = 241.70
        elif attackboost == 12:
          attackfood = 227.60
        elif attackboost == 13:
          attackfood = 209.30
        elif attackboost == 14:
          attackfood = 186.40
        elif attackboost == 15:
          attackfood = 158.60
        elif attackboost == 16:
          attackfood = 125.70
        elif attackboost == 17:
          attackfood = 88.00
        elif attackboost == 18:
          attackfood = 45.90
        else:
          attackfood = 0

        if defbonus < 8:
          defgold = 99.55
        elif defbonus == 8:
          defgold = 98.10
        elif defbonus == 9:
          defgold = 95.70
        elif defbonus == 10:
          defgold = 91.45
        elif defbonus == 11:
          defgold = 85.57
        elif defbonus == 12:
          defgold = 77.70
        elif defbonus == 13:
          defgold = 67.50
        elif defbonus == 14:
          defgold = 54.80
        elif defbonus == 15:
          defgold = 39.30
        elif defbonus == 16:
          defgold = 21.00
        else:
          defgold = 0

        if statsforallies < 8:
          statsforalliesgold = 99.55
        elif statsforallies == 8:
          statsforalliesgold = 98.10
        elif statsforallies == 9:
          statsforalliesgold = 95.70
        elif statsforallies == 10:
          statsforalliesgold = 91.45
        elif statsforallies == 11:
          statsforalliesgold = 85.57
        elif statsforallies == 12:
          statsforalliesgold = 77.70
        elif statsforallies == 13:
          statsforalliesgold = 67.50
        elif statsforallies == 14:
          statsforalliesgold = 54.80
        elif statsforallies == 15:
          statsforalliesgold = 39.30
        elif statsforallies == 16:
          statsforalliesgold = 21.00
        else:
          statsforalliesgold = 0

        if bonusforallies < 8:
          bonusforalliesgold = 99.55
        elif bonusforallies == 8:
          bonusforalliesgold = 98.10
        elif bonusforallies == 9:
          bonusforalliesgold = 95.70
        elif bonusforallies == 10:
          bonusforalliesgold = 91.45
        elif bonusforallies == 11:
          bonusforalliesgold = 85.57
        elif bonusforallies == 12:
          bonusforalliesgold = 77.70
        elif bonusforallies == 13:
          bonusforalliesgold = 67.50
        elif bonusforallies == 14:
          bonusforalliesgold = 54.80
        elif bonusforallies == 15:
          bonusforalliesgold = 39.30
        elif bonusforallies == 16:
          bonusforalliesgold = 21.00
        else:
          bonusforalliesgold = 0

        if marchboost < 8:
          marchboostgold = 99.55
        elif marchboost == 8:
          marchboostgold = 98.10
        elif marchboost == 9:
          marchboostgold = 95.70
        elif marchboost == 10:
          marchboostgold = 91.45
        elif marchboost == 11:
          marchboostgold = 85.57
        elif marchboost == 12:
          marchboostgold = 77.70
        elif marchboost == 13:
          marchboostgold = 67.50
        elif marchboost == 14:
          marchboostgold = 54.80
        elif marchboost == 15:
          marchboostgold = 39.30
        elif marchboost == 16:
          marchboostgold = 21.00
        else:
          marchboostgold = 0

        if abilityboost < 8:
          abilityboostgold = 99.55
        elif abilityboost == 8:
          abilityboostgold = 98.10
        elif abilityboost == 9:
          abilityboostgold = 95.70
        elif abilityboost == 10:
          abilityboostgold = 91.45
        elif abilityboost == 11:
          abilityboostgold = 85.57
        elif abilityboost == 12:
          abilityboostgold = 77.70
        elif abilityboost == 13:
          abilityboostgold = 67.50
        elif abilityboost == 14:
          abilityboostgold = 54.80
        elif abilityboost == 15:
          abilityboostgold = 39.30
        elif abilityboost == 16:
          abilityboostgold = 21.00
        else:
          abilityboostgold = 0

        if marchcap2 < 8:
          marchgold2 = 99.55
        elif marchcap2 == 8:
          marchgold2 = 98.10
        elif marchcap2 == 9:
          marchgold2 = 95.70
        elif marchcap2 == 10:
          marchgold2 = 91.45
        elif marchcap2 == 11:
          marchgold2 = 85.57
        elif marchcap2 == 12:
          marchgold2 = 77.70
        elif marchcap2 == 13:
          marchgold2 = 67.50
        elif marchcap2 == 14:
          marchgold2 = 54.80
        elif marchcap2 == 15:
          marchgold2 = 39.30
        elif marchcap2 == 16:
          marchgold2 = 21.00
        else:
          marchgold2 = 0
    totalgold = round(xpgold + gathergold + attackgold + marchgold + defgold + statsforalliesgold + bonusforalliesgold + marchboostgold + abilityboostgold + marchgold2, 2)
    totalfood = round(attackfood,2)
    totalore = round(defore,2)

    return render(request, 'calculators/MasteryCalculator.html', {'form': form, 'xpgold': xpgold, 'gathergold': gathergold, 
    'attackgold': attackgold, 'marchgold': marchgold, 'defore': defore, 'attackfood': attackfood, 'defgold': defgold, 
    'statsforalliesgold': statsforalliesgold, 'bonusforalliesgold': bonusforalliesgold, 'marchboostgold': marchboostgold, 
    'abilityboostgold': abilityboostgold, 'marchgold2': marchgold2, 'totalgold': totalgold, 'totalfood': totalfood, 'totalore': totalore})
  else:
    form = MasteryCalculatorForm()       
    return render(request, 'calculators/MasteryCalculator.html', {'form': form})