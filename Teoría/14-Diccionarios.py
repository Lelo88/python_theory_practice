#Un diccionario es una coleccion de datos especificada por una clave y un valor.
#Las claves suelen ser enteros o strings, aunque cualquier otro objeto inmutable puede actuar como variable
#Los valores pueden ser cualquier tipo de objeto

colores = {"rojo": "red", "azul": "blue", "amarillo": "yellow"}
print(colores["rojo"]) #imprimo el valor

#Al igual que las listas, los diccionarios son mutables
colores["amarillo"] = "white"
print(colores["amarillo"]) #ahora amarillo vale white

#Tambien permite asignacion
edades = {"Juan": 32, "Maria": 29, "Dario":31}
edades["Juan"]+=2
print(edades["Juan"])

#Funciones en diccionarios
#Para agregar elementos no existe una funcion, pero podemos realizarlo de la siguiente manera: 

numeros = {"uno":1,"dos":2,"tres":3}
print(f'Antes: {numeros}')
numeros["cuatro"] = 4
print(f'Ahora: {numeros}')


#update: actualiza un diccionario, agregando pares clave-valor
numeros.update({"cinco":5,"seis":6})
print(f'Ahora, despues del update: {numeros}')
otroNum = {"siete":7}
numeros.update(otroNum)
print(f'Ahora, despues del update con variable: {numeros}')

#funcion len
print(f'Tamaño actual del diccionario: {len(numeros)}')

#funcion del
del numeros["uno"] 
print(f'diccionario despues de eliminar el uno: {numeros}')

#determinar si un elemento se encuentra dentro de un diccionario
print("dos" in numeros)
print("ocho" in numeros)

numeros.clear() #limpia todo el diccionario
print(f'Ahora se ve asi el diccionario: {numeros}')