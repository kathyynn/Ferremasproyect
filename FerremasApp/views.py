from django.shortcuts import render
import mercadopago
import uuid
import json
import requests
from django.http import JsonResponse

# Create your views here.

def renderIndex(request):
    return render(request, 'FerremasApp/index.html')

def renderProducto(request):
    return render(request, 'FerremasApp/producto.html')

def renderLogin(request):
    return render(request, 'FerremasApp/login.html')

def renderSucursal(request):
    return render(request, 'FerremasApp/sucursal.html')

def renderBodegueros(request):
    return render(request, 'FerremasApp/bodegueros.html')

def renderSingle(request):
    return render(request, 'FerremasApp/single.html')

def renderCarroCompras(request):
    return render(request, 'FerremasApp/carro-compras.html')

def renderAdmin(request):
    return render(request, 'FerremasApp/admin.html')

def renderPortalPago(request):
    return render(request, 'FerremasApp/portal-pago.html')

def sendPage(request):
    ##Encargado de crear venta con los datos enviados en mercado pago
    sdk = mercadopago.SDK("TEST-5826808575170186-051116-0d09cb3bfd33a8edb88d8a90d6979956-462473584")

    request_options = mercadopago.config.RequestOptions()
    request_options.custom_headers = {
        'x-idempotency-key': str(uuid.uuid4())
    }

    payment_data = {
        "transaction_amount": float(request.POST.get("transaction_amount")),
        "token": request.POST.get("token"),
        "description": request.POST.get("description"),
        "installments": int(request.POST.get("installments")),
        "payment_method_id": request.POST.get("payment_method_id"),
        "payer": {
            "email": request.POST.get("email"),
            "identification": {
                "type": request.POST.get("type"), 
                "number": request.POST.get("number")
            }
        }
    }
    
    payment_response = sdk.payment().create(payment_data, request_options)
    payment = payment_response["response"]
    
    print(payment)


##Indicadores moneda
class Mindicador:
    def __init__(self, indicador, date):
        self.indicador = indicador
        self.date = date


def conversorMoneda(request):
    indicador = request.GET.get('indicador', None)
    date = request.GET.get('date', None)

    if indicador and date:
        url = f'https://mindicador.cl/api/{indicador}/{date}'
        response = requests.get(url)
        data = json.loads(response.text)
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Parámetros faltantes'}, status=400)