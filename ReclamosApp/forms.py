from django import forms
from ReclamosApp.models import Reclamos, Seguimiento


#class ReclamosFormulario (forms.Form):
#    suministro = forms.Select(label='Your name', required = True)
#    tipo_reclamo=forms.Select(label="Nombre", required=True)
#    detalle =forms.Textarea(label="Contenido", widget=forms.Textarea)


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
            "suministro" : forms.Select(attrs={'class':'form-control'}),
            "tipo_reclamo" : forms.Select(attrs={'class':'form-control'}), 
            "detalle" :  forms.Textarea(attrs={'class':'form-control'}), 
            #"imagen1": forms.FileField(attrs={'class':'form-control'}),
            #"imagen2": forms.FileField(attrs={'class':'form-control'}),
            
        }
        
class SeguimientoFrom(forms.ModelForm):
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
            "reclamo" : forms.Select(attrs={'class':'form-control'}),
        }
        
           