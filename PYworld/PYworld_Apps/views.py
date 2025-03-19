# miProyecto/views.py
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola mundo")

def fecha(request):
    import datetime
    ahora = datetime.datetime.now()
    return HttpResponse(f"<html><body><h2>Fecha y hora actual:</h2> {ahora}</body></html>")

def calcEdad(request, year):
    edadActual = 18
    periodo = year - 2025 # Se corrige el año base
    edadFutura = edadActual + periodo
    return HttpResponse(f"<html><body><h2>En el año {year} tendrás {edadFutura} años.</h2></body></html>")
