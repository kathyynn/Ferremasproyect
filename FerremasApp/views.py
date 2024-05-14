from django.shortcuts import render, redirect
import json
import requests
from django.http import JsonResponse
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, authenticate

# Create your views here.

def renderIndex(request):
    return render(request, 'FerremasApp/index.html')

def renderProducto(request):
    return render(request, 'FerremasApp/producto.html')

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

def renderPaxoExitoso(request):
    return render(request, 'FerremasApp/pago-exitoso.html')

def sendPage(request):
    ##Encargado de crear venta con los datos enviados en mercado pago
    print('asd')

def conversorMoneda(request):
    indicador = request.GET.get('indicador', None)
    date = request.GET.get('date', None)
    precio_final = request.GET.get('precioFinal', None)

    if indicador and date and precio_final:
        # Obtener el valor del indicador para la fecha dada
        url = f'https://mindicador.cl/api/{indicador}/{date}'
        response = requests.get(url)
        data = json.loads(response.text)
        if 'serie' in data and len(data['serie']) > 0:
            valor_indicador = data['serie'][0]['valor']

            # Convertir el precio final a la moneda del indicador
            precioConvertido = float(precio_final) / valor_indicador
            precio_final_redondeado = round(precioConvertido, 5)

            return render(request, 'FerremasApp/carro-compras.html', {'precioConvertido': precio_final_redondeado})
        else:
            return JsonResponse({'error': 'Parámetros faltantes'}, status=400)
    else:
        return JsonResponse({'error': 'Parámetros faltantes'}, status=400)
    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'FerremasApp/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'FerremasApp/login.html', {'form': form})