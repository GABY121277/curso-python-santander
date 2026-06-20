"""🧪 AUTORETO 4: Sistema de becas.

Reglas:

- Si la calificación es 90 o más:
    "Beca completa"

- Si la calificación es 80 o más:
    "Media beca"

- En cualquier otro caso:
    "Sin beca"

Instrucciones:

1. Crea una variable llamada calificacion.
2. Asigna un valor.
3. Usa if / elif / else.
4. Imprime el resultado.

"""

calificacion = 86

if calificacion >=90:
    print("Beca completa")
elif calificacion >=80:
    print("Media beca")
else:
    print("Sin beca")

"""🧪 AUTORETO 5: Descuento VIP.

Reglas:

- Si la compra es de $1000 o más:
    descuento = 150

- Si la compra es de $500 o más:
    descuento = 75

- En otro caso:
    descuento = 0

Imprime:

- descuento
- total final

Instrucciones:

1. Crea la variable compra.
2. Calcula el descuento.
3. Calcula el total.
4. Imprime ambos.

"""
compra = 467
descuento = 0
total = 0

if compra >= 1000:
    descuento = 150

elif compra >= 500:
    descuento = 75

else:
    descuento = 0

total = compra - descuento
print(descuento)
print(total)

"""🧪 AUTORETO 6: Acceso a evento.

Reglas:

Para entrar debe:

- Tener 18 años o más.
- Tener boleto.

Si cumple ambas:
    "Bienvenido"

Si no:
    "Acceso denegado"

Variables:

edad
boleto

"""
edad = 24
boleto = True

if edad >= 18 and boleto == True:
    print("Bienvenido")

else:
    print("Acceso denegado")


"""🧪 AUTORETO 7: Cliente Premium.

Reglas:

Cliente Premium si:

- Ha realizado 10 compras o más.

En otro caso:
- Cliente Normal

Variables:

compras_realizadas

"""

compras_realizadas = 35

if compras_realizadas >= 10:
    print("Cliente Premium")

else:
    print("Cliente Normal")

"""🧪 AUTORETO 8: Clasificación de temperatura.

Reglas:

temperatura >= 35
    "Hace mucho calor"

temperatura >= 20
    "Clima agradable"

En otro caso
    "Hace frío"

Variables:

temperatura

"""

temperatura = 9

if temperatura >= 35:
    print("Hace mucho calor")
elif temperatura >= 20:
    print("Clima agradable")
else:
    print("Hace frio")

    