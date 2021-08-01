from django.contrib import messages
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView

from .forms import TokenCalculator, BrewCalculator

def Index(request):
    return render(request, "index.html")

class TokenCalculator(FormView):
    template_name = 'TokenCalculator.html'
    form_class = TokenCalculator
    success_url = '/Token-Calculator'    

    def form_valid(self, form):
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
    
        messages.success(self.request, f"500: {token1:,}")
        messages.success(self.request, f"1k: {token2:,}")
        messages.success(self.request, f"2.5k: {token3:,}")
        messages.success(self.request, f"5k: {token4:,}")
        messages.success(self.request, f"10k: {token5:,}")
        messages.success(self.request, f"25k: {token6:,}")
        messages.success(self.request, f"50k: {token7:,}")
        messages.success(self.request, f"100k: {token8:,}")
        messages.success(self.request, f" 250k: {token9:,}")
        messages.success(self.request, f"500k: {token10:,}")
        messages.success(self.request, f"1m: {token11:,}")
        messages.success(self.request, f"Total: {token1+token2+token3+token4+token5+token6+token7+token8+token9+token10+token11:,}")
        
        return super().form_valid(form)

class BrewCalculator(FormView):
    template_name = 'BrewCalculator.html'
    form_class = BrewCalculator
    success_url = '/Brew-Calculator'    

    def form_valid(self, form):
        token1 = form.cleaned_data['token1'] * 10
        token2 = form.cleaned_data['token2'] * 25
        token3 = form.cleaned_data['token3'] * 50
        token4 = form.cleaned_data['token4'] * 100
        token5 = form.cleaned_data['token5'] * 250
    
        messages.success(self.request, f"10: {token1:,}")
        messages.success(self.request, f"25: {token2:,}")
        messages.success(self.request, f"50: {token3:,}")
        messages.success(self.request, f"100: {token4:,}")
        messages.success(self.request, f"250: {token5:,}")
        messages.success(self.request, f"Total: {token1+token2+token3+token4+token5:,}")
        
        return super().form_valid(form)