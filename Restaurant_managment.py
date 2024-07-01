import Restaurants
import almacenor
from almacenor import cliente
from Restaurants import client_rest
from Restaurants import producto



def cocina():
    factura = []
    client_rest.entrada = cliente.entrada
    if client_rest.entrada == 'vip':
        client_rest.cedulad = cliente.cedulad
        print(client_rest.factura(client_rest.nombre,client_rest.edad,client_rest.location))
        while True:
            x = input('Cual plato deseea pedir? \n')
            factura.append(x)
            k = input('Desea hacer otro pedido? \n')
            if k.lower() == 'no':
                print(f'Facturaccion: \n{'\n '.join(factura)} \nPrecio total: \n{str(int(producto.presio)*1.16)}')
                break
            elif k.lower() == 'si':
                continue


