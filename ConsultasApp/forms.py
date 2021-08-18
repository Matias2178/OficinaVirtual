from django import forms
from ConsultasApp.models import Consumo, Factura

class ConsumoForm (forms.ModelForm):
    class Meta:
        model = Consumo
        fields = [
            "suministro",
            "periodo",
            "consumo"
        ]
        label = {
            "Suministro": "suministro",
            "Periodo": "periodo",
            "Consumo": "consumo",
        }
        widgets ={
            "suministro": forms.Select(attrs={'class':'form-control',}),
        }