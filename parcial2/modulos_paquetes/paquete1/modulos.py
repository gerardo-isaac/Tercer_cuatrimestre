# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).
def borrar_pantalla():
    print("\033c")
def funcion1():
    nombre1=input("nombre: ").strip().upper() #.strip() sirve para quitar los espacios antes de que inicie la palabra o nombre,""  isaac", asi por ejemplo
    apellidos1=input("apellido: ").strip().upper()
    print(f"el nombre del alumno es: {nombre1} {apellidos1}")
def funcion3(nom,ape):
    nombre2=nom.upper()
    apellidos2=ape.upper()
    print(f"el nombre del alumno es: {nombre2} {apellidos2}")
 #2.- Funcion que no recibe parametros y regresa valor
def funcion2():
    nombre3="gerardo".upper().strip()
    apellido3="meza".upper().strip()
    return nombre3, apellido3

 #4.- Funcion que recibe parametros y regresa valor
def funcion4(nom, ape):
    nombre=nom
    apellido=ape
    return nombre, apellido