from django import forms
from PagosApp.models import Debito_Automatico


class DebitoAutomaticoFrom (forms.ModelForm):
    MM = forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control', 'type': 'text', 'size': '1'}))
    AA = forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control', 'type': 'text', 'size': '1'}))
    sel_banco = forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control', }))
    class Meta:
        model = Debito_Automatico
        fields = [
            "suministro",
            "tarjeta",
            "banco",
            "nombre",
            "numero_tarjeta",
            "vencimiento",
            "estado" ,          
        ]
        widgets = {
            "suministro" : forms.Select(attrs={'class':'form-control', 'type': 'seleccion'}),
            "tarjeta ": forms.Select(attrs={'class':'form-control', 'type': 'seleccion'}),
        }

class BajaDebitoAutomaticoFrom (forms.Form):
    suministro = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control', 'type': 'text'}))
        