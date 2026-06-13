# 1er utilizar los modulos 
import modulos

modulos.borrar_pantalla()
modulos.funcion1()
n="daniel"
a="perez"

nombre,apellidos=modulos.funcion4(n,a)
print(f"el nombre completo es: {nombre} {apellidos}")

#2da formar de utilizar modulos
from modulos import borrar_pantalla, funcion3, funcion4

borrar_pantalla()
n="daniel"
a="perez"
funcion3(n,a)

nombre,apellidos=funcion4
print(f"el nombre completo es: {nombre} {apellidos}")