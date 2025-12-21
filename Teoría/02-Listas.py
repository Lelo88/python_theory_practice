lista = [1,2,3, 'Una cadena']

print(lista[-1]) #puedo imprimir elementos a la inversa de la lista
print(lista[1])
print(lista[-2])

#concatenacion de listas

lista2 = [4,5,6,'Otra lista']
listaNueva = lista + lista2 # puedo unificar los listados anteriores en uno

print(listaNueva)

#mutabilidad de listas
listaPares=[0,2,4,5,8,10] #las listas son mutables, por lo que puedo cambiar el valor de una ubicación

listaPares[3] = 6 #en la posicion 3 de la lista cambiamos el valor

print(listaPares)

#asignación por slicing: puedo asignar a traves de un slicing elementos a una lista

listaPares [:3] = [12,14,16] #reemplazo los primeros tres números
print(listaPares)

#Borrado de elementos a través de slicing
listaPares[:3] =[]
print(f'lista de pares sin los primeros tres números: {listaPares}')

#borrado de elementos 
listaPares = []
print(f'Borrado de lista de números: {listaPares}')

#Funciones de listado
#append
listaNums=[1,2,3,4]
#listaNums.append(5)
#print(listaNums)

#tambien se pueden agregar append con calculo matematico:
#listaNums.append(5*4)
#print(f' Se agrega 5 * 4: {listaNums}')
#--------------------------
#len()->longitud de una lista: puedo saber cuantos elementos tiene un listado
print((f'cantidad de elementos de listaNums: {len(listaNums)}'))
#------------------
#pop -> elimina el ultimo elemento de una lista

listaNums.pop()
print(listaNums) #me elimina el numero 4 de la variable listaNums

nuevaListaNums = [1,2,1,3,4,1]
nuevaListaNums.pop(4) #me va a eliminar el primer elemento que encuentre con el dato indicado entre parentesis

print(nuevaListaNums)
#---------------
#index: nos indica el indice del valor en donde se encuentre en un listado
print(nuevaListaNums.index(2)) #me indica que el indice donde se encuentra 2
#-----------------
#count: nos indica el numero de veces que un valor se repite en la lista
print(nuevaListaNums.count(1)) #me va a indicar que el numero 1 se repite 3 veces

nuevalistaconrange = list(range(1,11))
print(nuevalistaconrange) #imprime los numeros del uno al 10 generados con range

matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(matriz) #una matriz es una lista de listas

chars = list('abc') #un listado de caracteres
print(chars)
