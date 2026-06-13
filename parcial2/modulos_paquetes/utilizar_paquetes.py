from paquete1 import modulos, modulo_paquete


modulos.borrar_pantalla()

nom="juan"
ape="polainas"

nombre, apellido=modulos.funcion4(nom,ape)
modulo_paquete.solicitar_edad()

print(f"el nombre de la persona es: {nombre}\nApellidos {apellido}\n edad: {modulo_paquete.solicitar_edad()}")

