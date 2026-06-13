# """
#  Sets.- 
#   Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

#   Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
# """
# print("\033c")
# set1={"phyton", " SQL", "estructurado"}
# print(set1)

# for i in set1:
#     print(i)

# set2={"hola", True, 33, 3.1416}
# print(set2)

# set2_respaldo=set2.copy()
# set2.clear()
# print(set2)
# print(set2_respaldo)

# set3={""}
# print(set3)

# set3.add("hola")
# set3.add(3)
# set3.add(10.0)
# set3.add("3")
# print(set3)
# set3.add(3)
# print(set3)


# set3.pop()
# set3.pop()
# print(set3)

# set3.clear()
# print(set3)

# lista=[10,9.5,8.5,3.4,8.5,10]
# print(lista)
# conjunto=set(lista)
# lista=list(conjunto)
# print(lista)
# #ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

# #solucion de clase
# lista_email=[]
# # set_emails={""}
# respuesta="si"
# while respuesta.lower()=="si":
#     lista_email.append(input("ingresa un email: ").lower().strip())
#     # set_emails.add(input("ingresa un email: ").lower().strip())

#     respuesta=input("¿deseas ingresar otro?: si/no").lower().strip()

# # print(set_emails)
# print(lista_email)
# set_emails=set(lista_email)
# lista_email=list(set_emails)
# print(lista_email)



# lista_email=[]
# respuesta=True
# while respuesta:
#     lista_email.insert(0, input("ingresa el email: "))
#     respuesta=input("¿deseas ingresar otro registro: ? ").lower().strip()
#     if respuesta=="no":
#         respuesta=False


# print(lista_email)
# set_emails=set(lista_email)
# lista_email=list(set_emails)
# print(lista_email)


















# #Solucion 1
# emails = set()

# cantidad = int(input("¿Cuántos emails quieres registrar? "))

# for i in range(cantidad):
#     email = input("Ingresa un email: ")
#     emails.add(email)

# print("Emails sin duplicados:")

# for email in emails:
#     print(email)

# #Solucion 2
# emails = set()
# respuesta = "si"

# while respuesta.lower() == "si":
#     email = input("Ingresa un email: ")
#     emails.add(email)

#     respuesta = input("¿Quieres ingresar otro email? si/no: ")

# print("Emails sin duplicados:")

# for email in emails:
#     print(email)



emails_s=[]
respuesta=True
while respuesta:
    emails_s.insert(0, input("ingresa un email: ").strip())
    respuesta=input("¿desea ingresar otro email: ? (SI/NO)").upper().strip()
    if respuesta=="NO":
        respuesta=False


set_email=set(emails_s)
lista_email=list(set_email)
print(lista_email)