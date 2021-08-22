from django import forms
from LiquidacionConveniosApp.models import Deuda
from OficinaVirtualApp.models import Suministro

class SuministroForm(forms.ModelForm):
    class Meta:
        model = Suministro
        fields =[
            "suministro"
        ]
        label = {
            "Suministro": "suministro"
        }
        widgets={
            "suministro": forms.Select(attrs={'class':'form-control',})
        }


class DeudaForm (forms.ModelForm):
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
            "suministro" : forms.Select(attrs={'class':'form-control'}),
            "documento" : forms.TextInput(attrs={'class':'form-control'}),
            "vencimiento" : forms.TextInput(attrs={'class':'form-control'}),
            "importe" : forms.TextInput(attrs={'class':'form-control'}),
            "estado" : forms.TextInput(attrs={'class':'form-control'}),
            
        }
            
    