import secrets

foo = {}
def generador(seat):
    code = secrets.token_hex(5)
    foo.update({seat:code})
    print (f'({code})')


def comprobador(seat,code):
    k = foo[seat] 
    if code == k:
        foo.pop(seat)
        print( f'El id del ticket ({code}) es valido')
    else:
        print(f'El id de su ticket es invalido o ya fue utilizado')
    

    
    


