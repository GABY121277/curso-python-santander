"""Autoejercicio 1:Operadores aritméticos.
a = 12
b = 5

| Expresión | Resultado |
| --------- | --------- |
| a + b     | 17        |
| a - b     | 7         |
| a * b     | 60        |
| a / b     | 2.4       |
| a // b    | 2         |
| a % b     | 2         |
| a ** b    | 248,832   |

"""

"""Autoejercicio 2:¿Qué imprime?
x = 20
y = 4

print(x + y) Imprime 24
print(x - y) Imprime 16
print(x * y) Imprime 80
print(x / y) Imprime 5 NOTA:5.0, es lo más correcto.

"""

"""Autoejercicio 3:Comparaciones.
Indica si el resultado es True o False.
a = 15
b = 10

| Expresión | Resultado |
| --------- | --------- |
| a == b    | False     |
| a != b    | True      |
| a > b     | True      |
| a < b     | False     |
| a >= b    | True      |
| a <= b    | False     |

"""
"""Autoejercicio 4:Operadores lógicos.

edad = 20
tiene_credencial = True

| Expresión                       | Resultado |
| ------------------------------- | --------- |
| edad >= 18 and tiene_credencial | True      |
| edad < 18 and tiene_credencial  | False     |
| edad >= 18 or tiene_credencial  | True      |
| not tiene_credencial            | False.    |

"""

"""Autoejercicio 5:Prioridad de operadores.
Clacula el resultado.

A
5 + 2 * 3
5 + 6 
11

B
(5 + 2) * 3
7 * 3
21

C
2 ** 3 + 1
8+1
9
"""

"""Autoejercicio 6:Detecta el error.

¿Qué error tiene este código?

a = 10
b = 5

resultado = a = b

Respuesta:b y a no son iguales, hay una contradicción a la hora de obtener el resultado.X
Respuesta correcta:La línea intenta hacer una asignación encadenada de forma incorrecta.Python marcará error de sintaxis.
resultado = (a == b).

"""
"""Autoejercicio 7:Problema real.
Una tienda vende un producto de $120.

Un cliente compra 3 unidades.

Calcula:

Total sin descuento.
Total con descuento de $50.

Declara variables y realiza las operaciones.

Completa:
precio = ______
cantidad = ______

total = ______

descuento = ______

total_final = ______

"""
precio = 120
cantidad = 3

total = 360

descuento = 50    

total_final =  310

#Autoejercicio 8: Sin ejecutar Python, indica el resultado:
resultado = (10 > 5) and (3 == 3) or (7 < 2)
#True,True,False.

#Autoejercicio 9:¿Qué mostrará?
a = 8
b = 3

print(a % b) #666666 X -> 2
print(a // b) #2     X -> 666666
print(a / b)  #2.66    -> Python muestra muchos decimales. 2.6666666666666665
print(a ** b) #512
