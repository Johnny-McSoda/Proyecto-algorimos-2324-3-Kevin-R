import secrets

dick = {}
def generador(seat):
    code = secrets.token_hex(5)
    dick.update({seat:code})
    print (f'({code})')


def comprobador(seat,code):
    k = dick[seat] 
    if code == k:
        dick.pop(seat)
        print( f'El id del ticket ({code}) es valido')
    else:
        print(f'El id de su ticket es invalido o ya fue utilizado')
    
generador('5A')
x = input('Metala ')
comprobador('5A',x.lower())

    
    


