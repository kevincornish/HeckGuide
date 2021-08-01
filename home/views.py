from django.contrib import messages
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView

from .forms import TokenCalculator

def Index(request):
    return render(request, "index.html")

class TokenCalculator(FormView):
    template_name = 'TokenCalculator.html'
    form_class = TokenCalculator
    success_url = '/Token-Calculator'    

    def form_valid(self, form):
        token1 = form.cleaned_data['token1']
        token2 = form.cleaned_data['token2']
        token3 = form.cleaned_data['token3']
        token4 = form.cleaned_data['token4']
        token5 = form.cleaned_data['token5']
        token6 = form.cleaned_data['token6']
        token7 = form.cleaned_data['token7']
        token8 = form.cleaned_data['token8']
        token9 = form.cleaned_data['token9']
        token10 = form.cleaned_data['token10']
        token11 = form.cleaned_data['token11']
    
        messages.success(self.request, f"500: {token1 * 500}")
        messages.success(self.request, f"1k: {token2 * 1000}")
        messages.success(self.request, f"2.5k: {token3 * 2500}")
        messages.success(self.request, f"5k: {token4 * 5000}")
        messages.success(self.request, f"10k: {token5 * 10000}")
        messages.success(self.request, f"25k: {token6 * 25000}")
        messages.success(self.request, f"50k: {token7 * 25000}")
        messages.success(self.request, f"100k: {token8 * 25000}")
        messages.success(self.request, f" 250k: {token9 * 250000}")
        messages.success(self.request, f"500k: {token10 * 500000}")
        messages.success(self.request, f"1m: {token11 * 1000000}")
        
        return super().form_valid(form)