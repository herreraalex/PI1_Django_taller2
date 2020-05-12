from django.shortcuts import render,  HttpResponse
import requests

# Create your views here.

# def home(request):
#    return render(request, "temphum/home.html")

def temphum(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': 'Grados Centigrados', 'value': value}
            response = requests.post('http://127.0.0.1:8000/temphum/', args)
            # Convierte la respuesta en JSON
            measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/temphum/')
    # Convierte la respuesta en JSON
    measures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "temphum/temphum.html", {'measures': measures})

    def cultivo(request):