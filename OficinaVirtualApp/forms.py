from django import forms
from OficinaVirtualApp.models import Cliente


class RecuperarClave(forms.Form):

    asunto = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'calle',
            'numero',
            'piso',
            'depto',
            'barrio',
            'factura'
        ]
        labels = {
            'calle': 'Calle', 
            'numero': 'Número',
            'piso': 'Piso',
            'depto': 'Departamento',
            'barrio': 'barrio',
            'factura': 'Factura', 
        }
        widgets = {
            'calle' : forms.TextInput(attrs = {'class':'form-control'}),
            'numero' : forms.NumberInput({'class':'form-control'}),
            'piso': forms.NumberInput({'class':'form-control'}),
            'depto': forms.TextInput({'class':'form-control'}),
        }
        
    
    

