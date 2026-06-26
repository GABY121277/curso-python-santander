"""Adivinando un número entre 1 y 10

generar (N° secreto) entre 1 y 10

mientras numero_del_jugador sea diferente de (N° secreto)

leer numero_del_jugador

if numero_del_jugador es mayor que (N° secreto) mostrar "Intente un número menor" de lo contrario si numero_del_jugador es menor que (N° secreto) mostrar "Intente un número mayor"

mostrar "Felicitaciones, ganaste"""

import random
num_secreto = random.randint(1,10)
numero_del_jugador = int(input(" Numero del jugador: "))

while numero_del_jugador != num_secreto:
    print(numero_del_jugador)

    if numero_del_jugador > num_secreto:
        print("Intente un numero menor" )
        
    else: 
        numero_del_jugador < num_secreto
        print("Intente un numero mayor")

    numero_del_jugador = int(input(" Numero del jugador: "))
print("Felicitaciones, ganaste")

    
