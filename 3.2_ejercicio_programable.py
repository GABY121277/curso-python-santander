# range() -> Genera una secuencia de números.range(5) -> 0,1,2,3,4 (el último número no se incluye)
# for -> Repite por cada elemento o número.Iniciando desde el 0, si no se le agrega un número de inicio, este caso también se agrega una i.
# while -> Repite mientras la condición sea verdadera.
# break -> Rompe el bucle.
# continue -> Salta a la siguiente iteración.
# pass -> No hace nada.

"""🧪 AUTORETO 1

Imprime los números del 1 al 20 usando un FOR.
"""

num = 0
for num  in range(1,21):
    print(num)

"""🧪 AUTORETO 2

Imprime los números del 10 al 1 usando un WHILE.

Pista:

contador = 10

"""
contador = 10
while True:
    print(contador)

    if contador == 1:
     break
    
    contador -= 1

"""🧪 AUTORETO 3

Una tienda quiere imprimir 5 veces el siguiente mensaje:

"Gracias por su compra"

Utiliza un FOR.

"""

for i in range(5):
   print("Gracias por su compra")


"""🧪 AUTORETO 4

Utiliza un WHILE para imprimir:

1
2
3
4
5

Cuando llegue a 5 debe terminar.

"""

num = 1
while num <= 5:
   print(num)

   if num == 5:
      break  
   num += 1


"""🧪 AUTORETO 5

Imprime los números del 1 al 10.

Pero cuando llegue al 6,
el programa debe detenerse utilizando BREAK.

"""
for contador in range(1,11):
   print(contador)

   if contador == 6:
      break
   
"""🧪 AUTORETO 6

Imprime los números del 1 al 10.

Pero NO debe imprimir el número 5.

Utiliza CONTINUE.

"""
num = 1
while True:
   if num == 5:
      num += 1
      continue
   print(num)
   if num == 10:
      break
   num += 1

   # Es más fácil hacerlo con un for, pero quise experimentar con while

   