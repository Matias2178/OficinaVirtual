from django import forms
from LiquidacionConveniosApp.models import Convenio, Deuda


class DeudaForm (forms.ModelForm):
    liquidar = forms.BooleanField(label="business", initial=False)
    class Meta:
        model = Deuda
        fields = [
            "suministro",
            "documento",
            "vencimiento",
            "importe",
            "estado",
        ]
        label = {
            "Suministro": "suministro",
            "Documento":  "documento",
            "Vencimiento": "vencimiento",
            "Importe": "importe",
            "Estado": "estado",
        }
        widgets = {
            "suministro" : forms.Select(attrs={'class':'form-control', 'type': 'seleccion'}),
            "documento" : forms.TextInput(attrs={'class':'form-control'}),
            "vencimiento" : forms.TextInput(attrs={'class':'form-control'}),
            "importe" : forms.TextInput(attrs={'class':'form-control'}),
            "estado" : forms.TextInput(attrs={'class':'form-control'}),
            
        }
            