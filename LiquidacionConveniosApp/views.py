from django.shortcuts import render, HttpResponse

# Create your views here.
def liquidacionDeuda(request):


    return render(request, "LiquidacionConveniosApp/liquidacionDeuda.html")

def convenioPago(request):

    return render(request, "LiquidacionConveniosApp/convenioPago.html")
