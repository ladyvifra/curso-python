''' ##1Control de flujo/Condicionales
##2 Expresiones Booleanas = clausura de puede ser evaluada como True o False

## 3- Operadores Relacionales= Comparan do sítems y returnan True o False, también llamados comparadores

##Primeros Operadores
##Igual ==
##Diferente !=

print(1 == 1)
#4- Variables booleanas
#5- Sentencias IF (preguntas)
bool_cuatro=2==2
if bool_cuatro:
  print("Sombrilla")
  
#mayor que >
#menor que <
#mayor o igual que  >=
#menor igual que <=
def chekear_edad(edad): 
  if edad > 13:
    return True
  elif edad >= 8:
    return "mayor o igual a 8"
  else:
    return False

print(chekear_edad(9))

#Operaciones booleanas: 
#and= Combina dos expresiones booleanas y evalua a True si AMBAS son True, d elo contrario devuelve False
print((1+1 == 2)and (2+ 2 == 4))
print((1+ 1 == 2)and (2< 1))

#or= Cobina dos expresiones booleanas a True SI CUALQUIERA DE LOS DOS ES TRUE
print((1+ 1 == 2) or (2< 1))
print((1+ 1 == 3)and (2< 1))

#not 
print(not True == True)

#7- Sentencias else y elif
def gracias (donacion):
  if donacion >= 10000:
    print("Gracias, su nivel es platium")
  elif donacion >=5000:
    print("Gracias, su nivel es gold")
  elif donacion >=1000:
    print("Gracias, su nivel es silver")
  else:
    print("Gracias, su nivel es bronce")
gracias(500) '''

#Ejercicio 12

def en_rango(num, inferior, superior):
  if num >=inferior and num < superior:
    return True
  else:
    return False
print(en_rango(5, 1, 10)) # True
print(en_rango(5, 6, 10)) # False
print(en_rango(1, 1, 10)) # True
print(en_rango(10, 1, 10)) # False

#Ejercicio 13

def calificar_pelicula(rating):
  if rating <= 5:
    return "Terrible!"
  elif rating > 5 and rating < 9:
    return "Interesante"
  elif rating >=9:
    return "Increíble"
  
print(calificar_pelicula(5)) # "Terrible!"
print(calificar_pelicula(8)) # "Interesante"
print(calificar_pelicula(9)) # "Increíble!"

#Ejercicio 14

def mas_del_doble(num1, num2):
  if num1 > (num2*2):
    return True
  else:
    return False

print(mas_del_doble(2, 5)) # True
print(mas_del_doble(5, 10)) # False

#Ejercicio 15

def gran_exponente (base, exponente):
  if base ** exponente > 5000:
    return True
  else:
    return False

# código de prueba
print(gran_exponente(2, 8)) # False
print(gran_exponente(5, 1000)) # False
print(gran_exponente(6, 900)) # True

#Ejercicio 16

def divisible_por_10(num):
  if num%10 ==0:
    return True
  else:
    return False
# código de prueba
print(divisible_por_10(100)) # True
print(divisible_por_10(1980)) # True
print(divisible_por_10(38)) # False

#Ejericico 17

def bing_bong(num):
  if (num % 3 == 0) and (num % 5 == 0):
    return "bingbong"
  elif num % 3 == 0:
    return "bing"
  elif num % 5 == 0:
    return "bong"
  else:
    return num
  
# código de prueba
print(bing_bong(3)) # "bing"
print(bing_bong(5)) # "bong"
print(bing_bong(30)) # "bingbong"
print(bing_bong(8)) # 8
