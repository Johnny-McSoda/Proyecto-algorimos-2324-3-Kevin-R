import per_vamp
import Comprobantes
import almacenor
from almacenor import cliente
import Restaurant_managment
cliente.nombre = input('Introduzca su nombre: \n')
cliente.cedulad = int(input('Introduzca su cedula (Sin puntos ni separaciones): \n'))
print(cliente.cedulad)
per_vamp.vampirico(int(cliente.cedulad))
cliente.edad = input('Y por ultimo introduzca su edad: \n')

print('Elija un partido:')
almacenor.filtrador()
part = int(input('Seleccione el Numero del partido que quiere comprar el ticket'))
cliente.partido = almacenor.responce_list_complete[part-1]


general_seats_available = []
VIP_seats_available = []

general_seats_occupied= []
VIP_seats_occupied = []

for i in range(1,16):
    for n in ['A','B','C','D']:
        general_seats_available.append(n+str(i))
    
for i in range(1,11):
    for n in ['X','Y']:
        VIP_seats_available.append(n+str(i))


while True:
    while True:
        cliente.entrada = input("Cual ticket deseea comprar? \n1.General \n2.VIP \n")
        if cliente.entrada.lower() == 'general':
            question = input('Quiere comprar la entrada General por 35$? \n')
            if question.lower() == 'si':
                 # Impresion del estadio
                print('*estadio* \n')
                seat = str(input(f'Seleccione el asiento que prefiera comprar: \n {'\n'.join(general_seats_available)} \n'))
                if seat.upper() in general_seats_available:
                    general_seats_occupied.append(seat)
                    general_seats_available.remove(seat)
                else:
                    input('Ese asiento no ya esta tomado o no existe')
                    continue
                print('Usted ha comprado exitosamente la entrada General')
                Original_price = 35.00
                break
            else:
                continue
        elif cliente.entrada.lower() == 'vip':
            question = input('Quiere comprar la entrada VIP por 75$? \n')
            if question.lower() == 'si':
                seat = str(input(f'Seleccione el asiento que prefiera comprar: \n {' '.join(VIP_seats_available)}'))
                if seat.upper() in VIP_seats_available:
                    VIP_seats_occupied.append(seat)
                    VIP_seats_available.remove(seat)
                else:
                    input('Ese asiento no ya esta tomado o no existe')
                    continue
                print('Usted ha comprado exitosamente la entrada VIP')
                Original_price = 75.00
                break
            else:
                continue
        else:
            continue


            
    if per_vamp.vampirico(cliente.cedulad):
        print('Se ha detectado que su Cedula es un numero vampiro por lo tanto el costo de su entrada se rebajara un 50%')
        Percental_price = Original_price*0.5
        Final_price = Original_price - Percental_price
        print(f'Por lo tanto su precio se ha rebajado a {str(Final_price)}$')
    else:
        Final_price = Original_price
        pass

    Final_price *= 1.16 
    print('Tambien se aplica el IVA (16%)')
    desition = input('Su asiento es '+str(seat)+', y el costo total es '+str(Final_price)+' desea proceder? \n')
    if desition.lower() == 'si':
        print('Su pago ha sido realizado exitosamente!!')
        break
    else:
        continue

print(f'Por motivos de seguridad al entrar al estadio tiene que presentar un codigo el cual es el siguente: ')
Comprobantes.generador(seat)


portero = input('Para entrar a al estadio introducir el codigo el cual le fue dado junto al ticket de su asiento: \n')
Comprobantes.comprobador(seat,portero)

Restaurant_managment.cocina()




