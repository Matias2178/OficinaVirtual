from django import forms


class RecuperarClave(forms.Form):

    asunto = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()


class DatosPersonales(forms.From):
    

