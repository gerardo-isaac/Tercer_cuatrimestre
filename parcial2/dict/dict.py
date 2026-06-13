"""

 dict.- 
  Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener como las listas indices numericos tiene alfanumericos. Es decir es algo parecido como los Objetos 

  Tambien se conoce como un arreglo asosiativo u Objeto JSON

  El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
"""

paises=["México","Brasil","Canada","España"]

pais1={
        "nombre":"México",
        "capital":"CDMX",
        "poblacion":12000000,
        "idioma":"español",
        "status":True
      }

pais2={
        "nombre":"Brasil",
        "capital":"Brasilia",
        "poblacion":14000000,
        "idioma":"portugues",
        "status":True
      }

pais3={
        "nombre":"Canada",
        "capital":"Otawua",
        "poblacion":10000000,
        "idioma":["ingles","frances"],
        "status":True
      }

print(pais1)

for i in pais1:
    print(f"{i}={pais1[i]}")

#Agregar un atributo a un objeto
pais1["altitud"]=3000
for i in pais1:
    print(f"{i}={pais1[i]}")

#Modificar un valor de un item o atributo que ya existe
pais1.update({"altitud":2500}) 
for i in pais1:
    print(f"{i}={pais1[i]}")

#Quitar el ultimo atributo de un objeto 
pais1.popitem() 
for i in pais1:
    print(f"{i}={pais1[i]}") 

#Quitar un atributo en especifico de un objeto 
pais1.pop("status") 
for i in pais1:
    print(f"{i}={pais1[i]}")











#Agregar un atributo a un objeto
print("\033c")

capitales={
  'Estados Unidos' : 'Washington D.C',
  'Argentina' : 'Buenos Aires',
  'chile' : 'Santiago De Chile',
  'Brasil' : 'Brasilia',
  'Brasil' : 'Brasilia'
}
print(capitales)

# #para agregar un valor al diccionario utilizamos:
capitales.update({'Alemania' : 'Berlin'})

print(capitales)

# #para sacar solo valos determinados, en este caso los estados son KEY y las capitales son VALUES, y tambien podemos
# #hacerles print uno a uno con la funcion get o todos con la funcion items pero seran separados por parentesis
print(capitales.values())
print(capitales.keys())
print(capitales.get('Argentina'))
print(capitales.items())

# #Modificar un valor de un item o atributo que ya existe

capitales['Brasil']='Rio de Janeiro'
print(capitales)

# #Quitar el ultimo atributo de un objeto 
capitales.popitem()
print(capitales)

# #Quitar un atributo en especifico de un objeto 
capitales.pop('Brasil')
print(capitales)