"""
Problema: Calcular el total de compras

Crea un programa que pida al usuario el precio de varios productos.
El programa debe terminar cuando el usuario escriba 0.

Debes crear una función llamada calcular_total(precio, total_actual) que reciba como parámetros:

precio: el precio del producto ingresado.
total_actual: el total acumulado hasta ese momento.

La función debe devolver el nuevo total.

Al final, el programa debe mostrar cuánto gastó el usuario en total.
"""

def limpiar_pantalla():
    print("\033c")

def multiplicar(num_1, num_2):
    resultado=num_1*num_2
    return resultado

limpiar_pantalla()
resultado=multiplicar(2, 4)

print(f"este es el resultado: {resultado}")