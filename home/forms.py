from django import forms


class TokenCalculatorForm(forms.Form):
    token1 = forms.IntegerField(label='500', initial=0)
    token2 = forms.IntegerField(label='1k', initial=0)
    token3 = forms.IntegerField(label='2.5k', initial=0)
    token4 = forms.IntegerField(label='5k', initial=0)
    token5 = forms.IntegerField(label='10k', initial=0)
    token6 = forms.IntegerField(label='25k', initial=0)
    token7 = forms.IntegerField(label='50k', initial=0)
    token8 = forms.IntegerField(label='100k', initial=0)
    token9 = forms.IntegerField(label='250k', initial=0)
    token10 = forms.IntegerField(label='500k', initial=0)
    token11 = forms.IntegerField(label='1m', initial=0)


class BrewCalculatorForm(forms.Form):
    token1 = forms.IntegerField(label='10', initial=0)
    token2 = forms.IntegerField(label='25', initial=0)
    token3 = forms.IntegerField(label='50', initial=0)
    token4 = forms.IntegerField(label='100', initial=0)
    token5 = forms.IntegerField(label='250', initial=0)


TROOPMIGHT_CHOICES =(
    ("1", "Train"),
    ("2", "Kill"),
)


class TroopMightForm(forms.Form):
    might = forms.IntegerField(label='Might', initial=0)
    trainkill = forms.ChoiceField(label='Train/Kill', choices=TROOPMIGHT_CHOICES)
    troops = forms.IntegerField(label='Troops', initial=0)

