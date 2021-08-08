from django import forms
from ReclamosApp.models import Reclamos


class ReclamosFrom (forms.ModelForm):
    suministro = forms.CharField(label='Suministro', required = True)
    tipo_reclamo = forms.CharField(label = 'Reclamo', required = True) 
    detalle =  forms.CharField(label = 'Contenido', widget = forms.Textarea)


#class ReclamosForm (forms.ModelForm):
#    
#    class Meta:
#        model = Reclamos
#        fields = [ 
#                  "suministro",
#                  "tipo_reclamo", 
#                  "detalle",
#                  "imagen1",
#                  "imagen2", 
#        ]
#        labels = {
#3            "Suministro" : "suministro",
#3            "Reclamo" : "tipo_reclao", 
#            "Detalle" : "detalle",
#            "Imagen 1" : "imagen1",
#            "Imagen 2" : "imagen2", 
#        }
#        widgets = {
#            "suministro" : forms.Select(attrs={'class':'form-control'}),
#            "tipo_reclamo" : forms.Select(attrs={'class':'form-control'}), 
#            "detalle" :  forms.TextInput(attrs={'class':'form-control'}),
#            "imagen1" : forms.ImageField(attrs={'class':'form-label'}),
#            "imagen2" : forms.ImageField(attrs={'class':'form-label'}),   
#        }
        

    
    