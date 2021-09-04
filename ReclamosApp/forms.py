from django import forms
from ReclamosApp.models import Reclamos, Seguimiento
from OficinaVirtualApp.models import Suministro
from django.contrib.auth.models import User

class ReclamosForm(forms.ModelForm):  
    class Meta:
        model = Reclamos
        fields = [ 
                  "suministro",
                  "tipo_reclamo", 
                  "detalle",
                  #"imagen1",
                  #"imagen2",            
        ]
        labels = {
            "Suministro" : "suministro",
            "Reclamo" : "tipo_reclamo", 
            "Detalle" : "detalle",
            #"Imagen 1": "imagen1",
            #"Imagen 2": "imagen2"
        }
        widgets = {
            "suministro" : forms.Select(attrs={'class':'form-control', 'type': 'seleccion'}),
            #"tipo_reclamo" : forms.Select(attrs={'class':'form-control'}), 
            #"detalle" :  forms.Textarea(attrs={'class':'form-control'}), 
            #"imagen1": forms.FileField(attrs={'class':'form-control'}),
            #"imagen2": forms.FileField(attrs={'class':'form-control'}),
            
        }
        
class SeguimientoFrom(forms.ModelForm):
    lista_reclamos = forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control', 'type': 'seleccion'}))
    class Meta:
        model = Seguimiento
        fields = [
            "reclamo",
            "fecha_novedad",
            "area",
            "observaciones",
            "estado",
        ]
        labels = {
            "Reclamo": "reclamo",
            "Ultima Acutalización": "fecha_novedad",
            "Area": "area",
            "Observaciones": "observaciones",
            "Estado": "estado",
        }
        widget = {
            "reclamo" : forms.Select(attrs={'class':'form-control', 'type': 'seleccion'}),
        }
        
           