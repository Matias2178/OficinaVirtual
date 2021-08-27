from django import forms
from ConsultasApp.models import Consumo, Factura
from OficinaVirtualApp.models import Suministro

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
            "suministro": forms.Select(attrs={'class':'form-control', 'type': 'seleccion'}),
        }
    #def ___init___(self, suministros, *args, **kwargs):
    #    self.suministro = suministros
    #    super(ConsumoForm, self).__init__(*args, **kwargs)
        

    
class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = [
            "suministro",
            "detalle_documento" ,
            "vencimiento_pri",
            "importe_pri",
            "vencimiento_seg",
            "importe_seg",
        ]
        label={
            "Suministro": "suministro",
            "Documento": "detalle_documento" ,
            "Pri_Vencimiento": "vencimiento_pri",
            "Pri_Importe": "importe_pri",
            "Seg_Vencimiento": "vencimiento_seg",
            "Seg_importe": "importe_seg",
        }
        widgets ={
            "suministro": forms.Select(attrs={'class':'form-control', 'type': 'seleccion'}),
        }
    
        