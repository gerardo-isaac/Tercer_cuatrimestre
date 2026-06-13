"""archivo para practicar lo que hemos visto de listas"""

#creacion de una lista
print("\033c")

lista_prueba=["hola","gerardo","Mexico","crear"]

#print (lista_prueba[3])

lista_prueba.append("isaac")
lista_prueba[0]="programacion" #cambia el dato que este en esa posicion
#print(lista_prueba)

for i in range (0,len(lista_prueba)):
    print(lista_prueba)