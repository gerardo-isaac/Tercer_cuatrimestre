7
"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""
#1.- Funcion que no recibe parametros y no regresa valor
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
    nombre4=nom
    apellido4=ape
    return nombre4, apellido4
nom, ape=funcion4("gerardo", "ramirez")
print(f"el nombre del alumno es: {nom} {ape}")
#Invocar las funciones
funcion1()

nombre=input("nombre: ").strip().upper()
apellidos=input("apellido: ").strip().upper()    
funcion3(nombre, apellidos)

nombre, apellidos=funcion2()
print=(f"el nombre del alumno es: {nombre} {apellidos}")

nombre=input("nombre: ").strip().upper()
apellidos=input("apellido: ").strip().upper()  
nom, ape=funcion4(nombre, apellidos)
print(f"el nombre del alumno es: {nom, ape}")