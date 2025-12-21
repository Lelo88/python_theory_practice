""""13-MetodosColecciones.py"""

VARIABLE = 'Una variable'
datos = {1, -5, 123.1, 34.32, 'Una cadena', 'Otra cadena', VARIABLE}
print(type(datos))

# Las listas son mutables, sin embargo, el set también es mutable,
# pero no podemos hacer slicing, ni manejar un set por índice.

# conjunto = {'a','b','c'}
# print(conjunto[:3])

# Funcion add: Agrega un nuevo item al set. Se pueden agregar operaciones matematicsa
numeros = {1, 2, 3, 4}
numeros.add(5)
print(numeros)

# Funcion update: Para añadir múltiples elementos a un set se usa la función update(), que
# puede tomar como argumento una lista, tupla, string, conjunto o cualquier objeto de tipo iterable.

numeros = {1, 2, 3, 4}
numeros.update([5, 6, 7, 8])  # Agregado de numeros por lista
numeros.update(range(9, 12))  # Agregado de numeros por range
print(numeros)

# Funcion len: mismo uso que en las listas y el los strings

print(len(numeros))

# Funcion discard: elimina el item del set sin modificar el resto del  set
# Tambien existe la funcion remove, pero la diferencia con discard es que si el elemento a eliminar
# no se encuentra, entonces la consola nos tira un error

numeros2 = {1, 2, 3, 4}
print(numeros2)

# in: determinamos si un elemento se encuentra en un conjunto:

print(2 in numeros2)  # tira true

# clear: sirve para borrar todos los elementos de un conjunto

# numeros2.clear()
# print(numeros2)

# pop: en este caso, elimina un elemento de forma aleatoria, ya que en los conjuntos los elementos no
# estan ordenados


while numeros2:
    print(f'se esta borrando: {numeros2.pop()}')


# lo que podemos hacer es convertir conjuntos en listados

primer = {1,1,2,2,3,4}
segundo = [3,4,5]
segundo = set(segundo) # puedo convertir el listado en un conjunto

print(primer | segundo) # union (no se repiten los datos en un set)
print(primer & segundo) # interseccion (devuelven los elementos que se encuentren en ambos sets)
print(primer - segundo) # diferencia (devuelven los elementos que se encuentren en el primer set pero no en el segundo)
print(primer ^ segundo) # diferencia (devuelven los elementos que se encuentren en el primer set y no en el segundo{1, 2, 3, 4, 5}
#{1, 2, 3, 4, 5}
#{3, 4}
#{1, 2}
#{1, 2, 5}