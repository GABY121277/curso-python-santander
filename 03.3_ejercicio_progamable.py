"""🧪 AUTORETO 9: Sistema de membresías.

Una tienda tiene tres tipos de clientes.

Reglas:

Cliente Platino:
- Compra >= 1500
- Y además es cliente frecuente.

Cliente Oro:
- Compra >= 800

Cliente Plata:
- Compra >= 300

En cualquier otro caso:
- Cliente Normal

Variables:

compra
cliente_frecuente

Instrucciones:

1. Declara las variables.
2. Usa if / elif / else.
3. Imprime el tipo de cliente.

"""

compra = 45
cliente_frecuente = False

if compra >= 1500 and cliente_frecuente == True:
    print("Cliente platino")
elif compra >= 800:
    print("Cliente Oro")
elif compra >= 300:
    print("Cliente Plata")
else:
    print("Cliente Normal")


"""🧪 AUTORETO 10: Acceso a un concierto.

Para entrar se necesita cumplir alguna de estas reglas:

Regla 1:
- Tener 18 años o más.

O

Regla 2:
- Tener permiso de los padres.

Si cumple cualquiera:
    "Puede entrar"

Si no:
    "No puede entrar"

Variables:

edad
permiso_padres

Pista:
Aquí tendrás que usar OR.

"""

edad = 13
permiso_padres = True

if edad >= 18 or permiso_padres == True :
    print("Puede entrar")

else:
    print("No puede entrar")

"""🧪 AUTORETO 11: Calculadora de descuentos PRO.

Una tienda tiene estas promociones.

Compra >= 2000
Descuento = 20%

Compra >= 1000
Descuento = 10%

Compra >= 500
Descuento = 5%

Compra menor a 500
Sin descuento.

Tu programa debe:

1. Declarar la variable compra.

2. Calcular el descuento.

3. Calcular el total final.

4. Imprimir:

Compra:
Descuento:
Total:

Ejemplo de salida:

Compra: 1500
Descuento: 0.1
Total: 1350

"""

compra = 500
descuento = 0
total = 0

if compra >= 2000 :
    descuento = 0.2

elif compra >= 1000 :
    descuento = 0.1

elif compra >= 500 :
    descuento = 0.05

else:
    descuento = 0    
total = compra - (compra * descuento) 
print("Compra:", compra, " Descuento: ", descuento, " Total: ", total)

    