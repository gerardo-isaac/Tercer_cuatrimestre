"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""
print("\033c")

#Funciones más comunes en las listas
paises=["Mexico","Canada","EUA","Mexico","Brasil"]

numeros=[23, 45, 8, 24]

varios=["hola", 3.1416, 33, True]

vacia=[]
#Imprimir el contenido de una lista
print(paises)

print(numeros)

print(varios)

print(vacia)

print(paises[1])
#Recorrer la lista 
#1er forma 

for i in paises:
     print(i)

# #2do forma 

for i in range(0,len(paises)):        #la funcion len() es para poder saber la cantidad de datos que se ingresaron en la lista 
     print(paises[i])

tamaño=len(paises)
for i in range(0, tamaño):
    print(paises)


#ordenar elementos de una lista

#ordenarlos de manera acendente
paises=["Mexico","Canada","EUA","Mexica","Brasil"]
print(paises)
paises.sort()
print(paises)

#ordenarlos de manera decendente

print(paises)
paises.reverse()
print(paises)
#dar la vuelta a una lista




#Agregar, insertar, Añadir un elemento a una lista
#1er forma 

paises.append("Honduras")
print(paises)

#2da forma

paises.insert(1,"Colombia")
print(paises)

paises.insert(8,"Australia")
print(paises)
#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma

paises.pop(4)
print(paises)

#2da forma 

paises.remove("EUA")
print(paises)

#Buscar un elemento dentro de la lista

resp="Brasil" in paises
print(resp)

if "Brasil" in paises:
     print("la respuesta es true")
else:
     print("la respuesta es false")
#Contar el numeros de veces que aparece un elemento dentro de una lista

numeros=[23, 45, 8, 24 ,100 ,200 ,0 ,-1 ,-10 ,23 ,24 ,8 ,23 ,50]
print(numeros)
numeros.sort()
print(numeros)

num=int(input("Dame un numero: "))
cuantos=numeros.count(num)
print(f"el numero de veces que aparece el {num} es de {cuantos} ")

# #Conocer la posicion o indice en el que se encuentra un elemento de la lista

posicion=numeros.index(100)
print(f"la posicion de numeros es: {posicion}")



#Unir el contenido de una lista dentro de otra lista

numeros=[23, 45, 8, 24 ,100 ,200 ,0 ,-1 ,-10 ,23 ,24 ,8 ,23 ,50]
print(numeros)
numeros2=[500,1000]
print(numeros2)

numeros.extend(numeros2)
print(numeros)

#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente

lista_prueba=[10,20,30,40,50]
lista_prueba2=[60,70,80,90,100]

print(lista_prueba)
print(lista_prueba2)

lista_prueba.extend(lista_prueba2)
print(lista_prueba)

lista_prueba.sort()
lista_prueba.reverse()
print(lista_prueba)

