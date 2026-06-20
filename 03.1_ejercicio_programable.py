"""🧪 AUTORETO 1: Clasificador de clientes (Shein Edition)
🎯 Objetivo:

Crear un programa que determine el tipo de cliente según su compra.

📌 Reglas:
-Si compra >= 800 → "Cliente Diamante"
-Si compra >= 300 → "Cliente Rosa"
-Si no → "Cliente Regular"
💻 Instrucciones:
1.Crea una variable llamada compra
2.Asigna un número (elige tú uno)
3.Usa if / elif / else
4.Imprime el resultado"""

compra = 850

if compra >= 800:
    print("Cliente Diamante")

elif compra >= 300:
    print("Cliente Rosa")

else:
    print(" Cliente regular")

"""🧪 AUTORETO 2: Sistema de acceso
🎯 Objetivo:

Decidir si una persona puede entrar.

📌 Reglas:
Si edad >= 18 y tiene credencial → "Acceso permitido"
Si no → "Acceso denegado"
💻 Instrucciones:
Variables:
edad
credencial (True o False)
Usa and
Usa if / else
Imprime resultado"""

edad = 20
credencial = False

if edad >=18 and credencial == True:
    print("Acceso permitido")
else:
    print("Acceso denegado")

"""🧪 AUTORETO 3: Mini calculadora de descuentos
🎯 Objetivo:

Calcular descuento según compra.

📌 Reglas:
compra >= 800 → descuento = 100
compra >= 300 → descuento = 50
else → descuento = 0
💻 Instrucciones:
Variable compra
Variable descuento
Condicionales
Imprime:
descuento
total (compra - descuento)
"""

compra = 234
descuento = 0
total = 0

if compra >= 800:
    descuento = 100

elif compra >= 300:
    descuento = 50

else:
    descuento

total = compra - descuento 
print(total)

#print(total(compra - descuento)) pq esta forma de hacer código no funciona? ->lo hacia fallar es que esta forma de escribir digamos que es exclusivamente para funciones

