import requests
import almacenor
from almacenor import stadium
from almacenor import URLstadiums
from almacenor import cliente

class restaurante(stadium):
    def __init__(self,Sname,location,StaCode,Rname):
        super().__init__(self,Sname,location,StaCode)
        self.Rname = Rname



class producto(restaurante):
    def __init__(self,Sname,location,StaCode,Rname,Pname,quantity,presio,stock,adicional):
        super().__init__(self,Sname,location,StaCode,Rname)
        self.Pname = Pname
        self.quantity = quantity
        self.presio = presio
        self.stock = stock
        self.adicional = adicional

        def __repr__(self):
            return f'{self.Rname}: {self.Pname}, Stock: {self.stock}, Aditional info: {self.adicional}'
        

class client_rest(cliente,producto):
    def __init__ (self,nombre,cedulad,edad,partido,entrada,Sname,location,StaCode,Rname,Pname,quantity,presio,stock,adicional,lista_productos,presio_total):
        cliente.__init__ (self,nombre,cedulad,edad,partido,entrada)
        producto.__init__(self,Sname,location,StaCode,Rname,Pname,quantity,presio,stock,adicional)
        client_rest.lista_productos = lista_productos
        client_rest.presio_total = presio_total

    def factura(self):
        return f'Facturacion: \nNombre: {self.nombre} \n edad: {self.edad} \n {self.location}:\n{self.Sname} \n{self.Rname} \n'





menu = []
producto.StaCode = 'sefheifhwe'

decodificador = requests.get(URLstadiums)
foo = decodificador.json()
for i in foo:
    for k in i["restaurants"]:
        restaurante.Rname = k["name"]
        for j in k["products"]:
            producto.Pname = j["name"]


            producto.quantity = j["quantity"]
            producto.presio = float(j["price"])*1.16
            #print(str(producto.presio))
            producto.stock = j["stock"]
            producto.adicional = j["adicional"]
            x = producto(producto.Sname,producto.location,producto.StaCode,producto.Rname,producto.Pname,producto.quantity,producto.presio,producto.stock,producto.adicional)
            menu.append(repr(x))
            print(' '.join(menu))



        

    
