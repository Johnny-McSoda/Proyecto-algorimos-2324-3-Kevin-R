#numero perfecto calculo

def perfeccionador(n):
    divisores = []
    n = int(n)
    if n > 1:
        print("El numero es mayor a 1")
        for i in range(1, n):
            if n % i == 0:
                divisores.append(i)
        
        k = 0
        for divisor in divisores:
            print("Divisor es igual a " + str(divisor))
            k += divisor
            print('k es igual a ' + str(k))
        
        if k == n:
            print(f"{n} es un número perfecto.")
        else:
            print(f"{n} no es un número perfecto.")
    else:
        print("Este numero no es valido")


def vampirico(numero):
    # Convertir el número en una cadena para trabajar con sus dígitos
    str_numero = str(numero)
    longitud = len(str_numero)
    
    # Los números vampiro deben tener un número par de dígitos
    if longitud % 2 != 0:
        return False
    
    # Obtener todos los pares posibles de colmillos
    for i in range(10**(longitud//2 - 1), 10**(longitud//2)):
        for j in range(i, 10**(longitud//2)):
            # Multiplicar los colmillos y verificar si el producto es igual al número original
            if i * j == numero:
                # Convertir los colmillos y el número en listas de dígitos y comparar
                if sorted(str(i) + str(j)) == sorted(str_numero):
                    return True
    return False

# Ejemplo de uso:
"""numero = int(input("Introduce un número para verificar si es vampiro: "))
if vampirico(numero):
    print(f"El número {numero} es un número vampiro.")
else:
    print(f"El número {numero} no es un número vampiro.")"""


