''' print("Hola, desde archivo 2")
frase= input("Escriba su nombre: ")
print(frase) '''

''' num1 = input("Ingrese número 1: ")
num2 = input("Ingrese número 2: ")

resultado = int(num1)+ int(num2)

#print(type(resultado))

print(resultado) '''

# interpolación
''' actual= 2021
nacimiento=int(input("Ingresa el año de nacimiento"))

edad= actual - nacimiento
print(edad)

print(f'Tienes:{edad} años') '''

#FUNCIONES

''' def nombre_de_la_funcion():

  pass

def saludar(mi_tienda, oferta_especial):
  print("Bienvenidos a mi tienda de camisetas "+ mi_tienda)
  print("La camiseta que tenemos en promoción es la de "+ oferta_especial)
  print("Disfruta comprando!")

saludar("Cómic Tienda","Star Wars") '''

## keyword arguments =palabra clave
## default arguments = argumentos por defecto

#Return

''' def dividir_por_4(numero):
  return numero/4

resultado=print(dividir_por_4(16))


def valor_al_cuadrado(valor_x, valor_y):
  x_2= valor_x * valor_x
  y_2= valor_y * valor_y
  return x_2, y_2

x_al_cuadrado, y_al_cuadrado = valor_al_cuadrado(1,3)

print(x_al_cuadrado, y_al_cuadrado)

## scope(alcance d ela variable)
#variable local
#variable global
articulo_especial= "zapato"
def crear_string(articulo_especial):
  return"Nuestro atículo especial es " + articulo_especial +"."

print("No me gusta el " + articulo_especial)
 '''

''' def suma (x, y):
  return(x+y)

# código de prueba, verifica que aparezcan los valores correctos en la consola

print(suma(1, 2)) # 3
print(suma(0, 0)) # 0
print(suma(245, 923)) # 1168 '''

## Ejercicio 7


''' # escribe la función hola acá
def hola(nombre):
  return (f"Hola {nombre}!")

# código de prueba
print(hola("Pedro")) # "Hola Pedro!"
print(hola("Juan")) # "Hola Juan!"
print(hola("")) # "Hola !" '''

#Ejercicio 8

''' def raiz_cuadrada(num):
  return num**0.5

# código de prueba
print(raiz_cuadrada(25)) # 5.0
print(raiz_cuadrada(5476)) # 74.0
print(raiz_cuadrada(2)) # 1.4142135623730951 '''

#Ejercicio 10

''' def porcentaje_de_victorias(victorias, derrotas):
  porcentaje_de_victorias= (100*victorias)/(victorias+derrotas)
  return (f"El porcentaje de victorias es del:{porcentaje_de_victorias}%")

print(porcentaje_de_victorias(5, 5)) # 50
print(porcentaje_de_victorias(7, 0)) # 100
print(porcentaje_de_victorias(6000, 4000)) # 60 '''

#Ejercicio 11

def edad_perruna(nombre, edad):
  return(f"{nombre}, tienes {edad*7} en años perrunos")


print(edad_perruna("Pedro", 20)) # 140
print(edad_perruna("Maria", 8)) # 56
print(edad_perruna("Alex", 45)) # 315


