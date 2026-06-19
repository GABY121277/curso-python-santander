"""Autoejercicio 1: Identifica las variables

nombre = "Carlos"
edad = 22
altura = 1.80

| Variable | Valor   |
| -------- | ------- |
| nombre   | Carlos  |
| edad     | 22      |
| altura   | 1.80    |

"""

"""
Autoejercicio 2: ¿Cuál será el valor? X -> Esto funciona igual que en asignación múltiple

a = 5
b = a
c = b

| Variable | Valor   |
| -------- | ------- |
| a        | 5       |
| b        | a       |
| c        | b       |

"""

"""Autoejercicio 3: Asignación múltiple
x = y = z = 100

| Variable | Valor   |
| -------- | ------- |
| x        | 100     |
| y        | 100     |
| z        | 100     |

"""

"""Autoejercicio 4:Variables válidas o inválidas.

| Nombre de variable | ¿Válida? |
| ------------------ | -------- |
| edad               | si       |
| 1edad              | no       | Las variables en python NO pueden iniciar con un número
| nombre_completo    | si       |
| total-ventas       | no       | Las variables en python NO pueden tener -
| _contador          | no       | Las variables en python NO pueden iniciar con un _ X ->En Python es totalmente válido
| while              | no       | Las variables en python NO pueden usar el nombre de una palabra reservada
| precio2025         | si       |


"""

"""Autoejercicio 5:Corrige los nombres inválidos.

1edad = 18
nombre-completo = "Juan Pérez"
for = 10

"""
edad = 18
nombre_completo = "Juan Pérez"
num = 10

"""Autoejercicio 6:Crea variables,
Imagina que estás creando un sistema para una tienda.

Declara variables para:

Nombre del producto
Precio
Cantidad disponible
Producto en oferta (True o False)
"""

Nombre_Producto = 'Sapito'
Precio_Producto = 10
Cantidad_Producto = 20
Oferta_Producto = False

#Autoejercicio 7:¿Cuáles de estas parejas representan variables diferentes?
nombre 
Nombre
#Diferentes, python es sensible a las mayúsculas

edad
Edad
#Diferentes, python es sensible a las mayúsculas

precio
precio
#Iguales

"""Autoejercicio 8:¿Qué errores encuentras aquí?
nombre completo = "Ana"
2precio = 50
if = True
"""
nombre_completo = "Ana"
precio = 50
comprar = True

#NOTA:True y False, siempre inician con mayúsculas.
#Una variable guarda el valor, no el nombre de otra variable.
#Las variables sí pueden comenzar con _.
