"""🧪 RETO 1: Contador de números.

Pide al usuario un número.

Imprime desde 1 hasta ese número usando WHILE.

Ejemplo:

Número: 5

1
2
3
4
5

"""
i = 1
num = int(input("Ingrese un numero: "))
while i <= num:
    print(i)
    i+=1

"""🧪 RETO 2: Tabla de multiplicar.

Pide un número al usuario.

Imprime su tabla de multiplicar del 1 al 10.

Ejemplo:

Número: 7

7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70

"""

num = int(input("Ingrese un numero:"))
for i in range(1,11):
    print(num, "X ", i, "=", num*i)

   
"""🧪 RETO 3: Suma de números.

Pide un número al usuario.

Calcula la suma desde 1 hasta ese número.

Ejemplo:

Número: 5

1 + 2 + 3 + 4 + 5 = 15

"""
cont = 0
i = 1
num = int(input("Ingrese un numero: "))

while i<=num:
    print(i,"+")
    i += 1
    cont += i
print("=",cont)
#Pendiente


    

