from django.contrib import admin
from django.urls import path
from FerremasApp.views import renderIndex, renderProducto, renderLogin, renderSucursal, renderBodegueros, renderSingle, renderCarroCompras

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', renderIndex),
    path('index/', renderIndex),
    path('producto/', renderProducto),
    path('login/', renderLogin),
    path('sucursal/', renderSucursal),
    path('bodegueros/', renderBodegueros),
    path('single/', renderSingle),
    path('carro-compras/', renderCarroCompras)
]
