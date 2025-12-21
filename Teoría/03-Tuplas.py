#las tuplas son variables similares a las listas, solo que estas son inmutables
#se utlizan parentesis en lugar de corchetes para definirlas
#no tienen restricciones sobre los tipos de datos que se ingresen

miTupla = (1,2,3,4)

#si queremos declarar una tupla con un unico valor: 
nuevaTupla = ("hola",)

#funcionan de igual manera con el indice y con el slicing

print(miTupla[0])
print(miTupla[1:3])

#las tuplas se pueden concatenar
print(miTupla + nuevaTupla)

#la funcion append no funciona en tuplas, pero se pueden agregar datos de esta manera
miTupla += ('hola','mundo',7,8,10,9)
print(miTupla)

#como las listas son mutables y las tuplas no, estas ultimas no pueden modificarse
#miTupla[1] = 10

#FUNCIONES DE TUPLAS
#len (como en las listas)

print(len(miTupla))

#count (como en las listas) -> cuenta la cantidad de veces que se repite un numero
print(miTupla.count(7))

#index (como en las listas) -> nos indica el indice donde se encuentra el elemento
print(miTupla.index(7))

#----------------------

# podemos iterar una tupla como si fuera un listado, PERO NO SE PUEDE MODIFICAR LOS ELEMENTOS QUE SE ENCUENTRAN 
# DENTRO DE ELLA

numeros = (1,2,3,4)

for num in numeros:
    print(num)
    
# lo que si puedo hacer es convertir la tupla a una lista para poder modificarla (no originalment, por la propia definicion de la tupla)

listaNumeros = list(numeros)
print(listaNumeros)

listaNumeros[0] = 10
print(listaNumeros)
    
    