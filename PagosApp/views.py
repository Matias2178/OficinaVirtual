
from django.shortcuts import render, HttpResponse
from datetime import date
from OficinaVirtualApp.models import Suministro
from PagosApp.models import Debito_Automatico

def botonPago(request):


    return render(request, "PagosApp/botonPago.html")

def debitoAutomatico(request):
    suministros = Suministro.objects.all() #cambiar a filtro
    fecha = date.today()
    anios = range(fecha.year, (fecha.year + 15))
    
    meses = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre","Noviembre", "Diciembre")
    
    bancos = ( "NUEVO BANCO DE SANTA FE S.A." ,"BAN SUD","BANCO MACRO S.A.","BANCO SANTANDER RÍO S.A.",
              "BBVA BANCO FRANCES S.A.","CITIBANK","BANCO DE LA NACIÓN ARGENTINA","BANCO PROV. DE BUENOS AIRES",
              "ICBC - BANK CHINA","BANCO PROV. DE CÓRDOBA","BANCO SUPERVIELLE S.A.","BANCO CIUDAD DE BUENOS AIRES",
              "BANCO PATAGONIA S.A.","BANCO HIPOTECARIO S.A.","BANCO DE SAN JUAN S.A.","BANCO TUCUMÁN S.A.",
              "BANCO MUNICIPAL DE ROSARIO","BANCO DEL CHUBUT S.A.","BANCO DE SANTA CRUZ S.A.",
              "BANCO DE LA PAMPA SOCIEDAD DE ECONOMÍA MIXT","BANCO DE CORRIENTES S.A.","BANCO PROVINCIA NEUQUÉN","HSBC BANK ARGENTINA S.A.","BANCO CREDICOOP COOP.LTDO.","BANCO ITAÚ ARGENTINA S.A.","BANCO PROV.DE TIERRA DEL FUEGO","BANCO REPÚBLICA O. DEL URUGUAY","BANCO COMAFI SOCIEDAD ANÓNIMA","BANCO RIOJA SOCIEDAD ANÓNIMA UNIPERSONAL","NUEVO BANCO DEL CHACO S.A.","BANCO DE FORMOSA S.A.", "BANCO DE SANTIAGO DEL ESTERO S.A.","NUEVO BANCO DE ENTRE RÍOS S.A.""BANCO BICA S.A.","DESCONOCIDO")
    
    tarjetas = ("VISA – TARJETA DE CRÉDITO", "MASTERCARD", "VISA – TARJETA DE DÉBITO", "CABAL")

    lista = {"aios": anios,
             "meses": meses,
             "bancos": bancos,
             "tarjetas": tarjetas,
             "suministros": suministros
            }
      
    
    return render(request, "PagosApp/debitoAutomatico.html",lista)


def bajaDebitoAutomatico(request):
    suministros = Suministro.objects.all() #cambiar a filtro
    debitos = Debito_Automatico.objects.all() #cambiar a filtro
    
    dic = {"suministros": suministros,
           "debitos": debitos
           }
    
    return render(request, "PagosApp/bajaDebitoAutomatico.html",dic)
