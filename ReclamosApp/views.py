from django.shortcuts import render, HttpResponse


def reclamos(request):
    return render(request, "ReclamosApp/reclamos.html")


def seguimientoReclamos(request):
    return render(request, "ReclamosApp/seguimientoReclamos.html")

