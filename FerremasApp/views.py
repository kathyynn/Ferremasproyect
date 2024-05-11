from django.shortcuts import render

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