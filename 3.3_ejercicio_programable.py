"""🧪 AUTORETO 7: Contador de pares.

Imprime todos los números del 1 al 20.

Pero solamente deben mostrarse los números pares.

No puedes escribir los números manualmente.

Pista:
Recuerda el operador %.

"""

for num in range (1,21):
    op = num % 2

    if op == 0:
        print(num)


"""🧪 AUTORETO 8: Cuenta regresiva.

Haz un programa que imprima:

10
9
8
...
1

Al terminar debe imprimir:

"¡Despegue!"

Utiliza WHILE.

"""
cuenta = 10
while cuenta >= 1:
    print(cuenta)
    cuenta -= 1
    continue #No entiendo pq funciona mal con break
print("¡Despegue!")

"""🧪 AUTORETO 9: Tabla del 5.

Imprime la tabla de multiplicar del 5.

Debe mostrarse así:

5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50

Utiliza FOR.

"""
for tabla in range(1,11):
    print("5 X ", tabla,"=", 5 * tabla )

"""🧪 AUTORETO 10: Contador de compras.

Imagina que una tienda quiere imprimir:

Compra #1 registrada
Compra #2 registrada
...
Compra #15 registrada

Utiliza FOR.

"""

for compra in range(1,16):
    print("Compra #",compra, "registrada")
    
"""🧪 AUTORETO 11: Saltando múltiplos.

Imprime los números del 1 al 20.

Pero NO deben imprimirse:

5
10
15
20

Utiliza CONTINUE.

(No escribas varios if.
Intenta resolverlo con una sola condición.)

"""

for mult in range(1,21):
    if mult % 5 == 0:
        continue
    else:
        print(mult)

"""🧪 AUTORETO 12: Buscar el premio.

Imprime los números del 1 al 100.

Pero cuando llegues al 37:

Imprime:

"¡Premio encontrado!"

Y termina inmediatamente el programa.

Utiliza BREAK.

"""
for num in range(1,101):
    print(num)
    if num == 37:
        print("Premio encontrado")
        break

"""🧪 SUPER RETO

Una tienda quiere generar los tickets.

Debe imprimir del 1 al 20.

Pero:

- Si el número del ticket es múltiplo de 4,
  NO debe imprimirse.

- Cuando llegue al ticket 17,
  debe imprimir:

"Último ticket especial"

y terminar el programa.

Utiliza:

FOR
CONTINUE
BREAK

Todo en un mismo programa.

"""
for ticket in range(1,21):
    if ticket % 4 == 0:
        continue
    elif ticket == 17:
        print("Ultimo ticket especial")
        break
    else:
        print(ticket)

"""🧪 RETO EXTREMO

Imprime del 1 al 30.

Pero:

- No imprimir múltiplos de 3.
- Detenerse al llegar al 22.
- Al final imprimir:

"Programa terminado"

Utiliza:

FOR
CONTINUE
BREAK

"""
for mult in range(1,31):
    if mult % 3 == 0:
        continue
    elif mult == 22:
        break
    else:
        print(mult)
    continue
print("Programa terminado")
# range() -> Genera una secuencia de números.range(5) -> 0,1,2,3,4 (el último número no se incluye)
# for -> Repite por cada elemento o número.Iniciando desde el 0, si no se le agrega un número de inicio, este caso también se agrega una i.
# while -> Repite mientras la condición sea verdadera.
# break -> Rompe el bucle.
# continue -> Salta a la siguiente iteración.
# pass -> No hace nada.
