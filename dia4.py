''' #Listas: set ordenados de objetos en python. Tipo de datos
#Una lista empieza y termina []
#Cada elemento va separado por comas. Es buena práctica añadir un espacio después de cada coma.
alturas=[1.9, 1.7, 1.5, 1.2, 1.3]


nombres=["Ana", "Pablo", "Rosa", "Laura", "Pedro"]
mix=[12, "Juan", True]

print(alturas)
print(nombres)
print(mix)

#Las listas pueden contener otras Listas
list_list=[["Ana", 13], ["Juan", 25], ["Pablo", 37]]
##Listas vacias
lista_vacia = []
#Llenar una lista, vacias o con valores
##1- .append() Solo puede añadir un elemento a la lista_vacia

lista_vacia.append(1)
print(lista_vacia)

##2- Añadir múltiples valores. Operador +- polimorfismo:Una misma función sirve para diferentes tipos d eoperadores
lista_con_valores = [2.3, "Ruth", 3]
lista_vacia += lista_con_valores
print(lista_vacia)

##Índices de las lista
alturas = [1.9, 1.7, 1.5, 1.4, 1.3]
nombres = ["Ana", "Juan", "Pablo", "Roberto", "Sonia"]
#Selección de un elemento basado en su Índices

print(alturas[2])

#editar , cambiar un valor en la lista ## Las listas son mutables

alturas[1]= 2.1
print(alturas)

#Ver si existe un elemento dentro de la lista.   
print(1.9 in alturas)

if 1.9 in alturas:
  print("sí se encuentra el valor")
else:
  print("No se encuentra ")

#Insert- Añade un valor en la posición deseada
#alturas.insert(0,1)
print(alturas)

## eliminar pop()- elimina el índice especificado. Si no le pasa ningún índice, elimina el último
alturas.pop(0)
print(alturas)

#del- elimina la lista completa
#vacias la lista- clear()
#alturas.clear()
#print(alturas)

#Métodos nativos de python-buscar



###slicing list

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#letras[indice]
#letras[inicio:fin]
#fin = valor -1
#fin = indice +1
sublista = letras[1:6]
print(sublista)

print(letras[:3])
print(letras[2:])
print(letras[-3:])
print(letras[:-3])


## Range, es un tipo de datos en python. Es diferente de las listas pero se relacionan.

mi_rango = range(10)  #Genera una lista desde 0 hasta un número antes
print(mi_rango)
mi_rango_list = list(mi_rango)

#lenght- Para saber cuántos elementos hay o el tamaño

print(mi_rango_list)
print(len(mi_rango_list))

ejemplos = ["rojo", "azul", "amarillo", "verde"]
print(len(ejemplos))

for color in range(len(ejemplos)):
  print(ejemplos[color])


#zip-- Para emparejar elementos de dos Listas. 

edades = [23, 45, 56, 13]
nombres = ["Gloria", "Roberto", "Nina", "Jorge"]

print(zip(edades, nombres))
print(list(zip(edades, nombres)))


## Ejercicios

## Ejercicio 18

nombres = ["Pedro", "Maria", "Pablo", "Diana"]
nombres.append("Juan")
for nombre in nombres:
  print(nombre)

#Ejercicio 19

def crear_rango(num):
  lista_vacia = []
  if num < 1:
    return (lista_vacia) 
  else:
    return  (list(range(1, num+1)))

print(crear_rango(5)) # [1, 2, 3, 4, 5]
print(crear_rango(1)) # [1]
print(crear_rango(0)) # []
print(crear_rango(-10)) # [] '''

## Ejrecicio 20

def longitud(lista):
  return len(lista)

print(longitud([1, 2])) # 2
print(longitud(['a', 'b', 'c', 'd', 'e'])) # 5
print(longitud([])) # 0


##Ejercicio 21


def combinar(a, b):
  return list(zip(a, b))

# código de prueba
print(combinar([1, 2], ['a', 'b'])) # [(1, 'a'), (2, 'b')]
print(combinar(["Pedro", "Maria"], [15, 22])) # [("Pedro", 15), ("Maria", 22)]

##Ejercicio 22


def ordenar(lista_numeros):
  lista_numeros.sort()
  return lista_numeros

  # código de prueba
print(ordenar([3, 2, 1])) # [1, 2, 3]
print(ordenar([5, 1, 8, 7])) # [1, 5, 7, 8]


#Ejercicio 23

def ultimo(lista):
  if len(lista)>1:
    return lista[-1]
  else:
    return "La lista está vacía"



# código de prueba
print(ultimo([3, 2, 1])) # 1
print(ultimo([5, 1, 8, 7])) # 7
print(ultimo([])) # "La lista está vacía"

### Ejercicio 24

nums = [1, 23, 5, 8, 40, 12, 2, 67, 24, 9, 39]

for num in nums:
  if num > 10:
    print (num)
  