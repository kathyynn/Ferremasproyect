from django.contrib import admin
from django.urls import path
from FerremasApp.views import renderIndex, renderProducto, renderSucursal, renderBodegueros, renderSingle, renderCarroCompras, renderAdmin, renderPortalPago, sendPage, conversorMoneda, register, login

urlpatterns = [
    ##Escuchador de cambios en la ruta, si detecta cambio, ejecuta funcion respectivo a la conincidencia encontrada
    path('admin/', admin.site.urls),
    path('', renderIndex),
    path('index/', renderIndex),
    path('producto/', renderProducto),
    path('sucursal/', renderSucursal),
    path('bodegueros/', renderBodegueros),
    path('single/', renderSingle),
    path('carro-compras/', renderCarroCompras),
    path('admin-contador/', renderAdmin),
    path('portal-pago/', renderPortalPago),
    path('process_payment/', sendPage),
    path('conversor-moneda/', conversorMoneda),
    path('register/', register, name='register'),
    path('login/', login, name='login')
]
