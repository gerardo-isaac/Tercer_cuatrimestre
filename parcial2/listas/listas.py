print("\033c")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros=[10, 34, 25, 45]
opc="si"
while opc=="si":
     numero=int(input("dame un numero: "))
     numeros.append(numero)
     opc=input("¿Deseas ingresar otro numero? (SI/NO)")

print(numeros)

lista="["
for i in numeros:
    lista+=f"{i}, "
    
print(f"{lista}]")

lista="["
for i in range(0,len(numeros)):
    lista+=f"{numeros [i]}, "
    
print(f"{lista}]")
lista="["
i=0

while i<len(numeros):
     lista+=f"{numeros [i]}, "
     i+=1
     print(f"{lista}]")

#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
palabras=("UTD", "segundo", "TI", "MTI")
print(palabras)   
palabra_buscar=input("dame una palabra a buscar: ").strip()

if palabra_buscar in palabras:
     print("encontre la palabra en la lista: ")
else: 
     print("no encontre la palabra en la lista ")


#2DA FORMA
palabras=("UTD", "segundo", "TI", "MTI")
print(palabras)   
palabra_buscar=input("dame una palabra a buscar: ").strip()

encontro=False
for i in palabras:
     if i==palabra_buscar:
         encontro=True 
if  encontro:
     print("encontre la palabra en la lista: ")
else: 
     print("no encontre la palabra en la lista ")

#3er FORMA
palabras=("UTD", "segundo", "TI", "MTI")
print(palabras)   
palabra_buscar=input("dame una palabra a buscar: ").strip()

encontro=False
for i in range(0,len(palabras)):
    if palabras[i]==palabra_buscar:
         encontro=True 
    if  encontro:
     print("encontre la palabra en la lista: ")
    else: 
     print("no encontre la palabra en la lista ")

#cuarta forma

palabras=("UTD", "segundo", "TI", "MTI")
print(palabras)   
palabra_buscar=input("dame una palabra a buscar: ").strip()

encontro=False
i=0
while i<len(palabras):
    if i==palabra_buscar:
        encontro=True
    i+=1 
if  encontro:
    print("encontre la palabra en la lista: ")
else: 
    print("no encontre la palabra en la lista ")


#Ejemplo 3 Añadir elementos a la lista



#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda

