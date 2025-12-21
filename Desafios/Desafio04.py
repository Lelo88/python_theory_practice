#Dadas dos listas LISTA1 y LISTA2 debes realizar las siguientes tareas:
# Añade a la LISTA1 el int 456789 y luego el string “Hola Mundo”
# Luego añade a la LISTA2 el string “Hola y Adios” y luego el int 5555
# Genera una LISTA3 con todos los elementos de la LISTA1 sin considerar el último elemento
# Genera una LISTA4 con todos los elementos de la LISTA2 menos el primero y el último elemento
# Finalmente, genera una LISTA5 con los elementos de la LISTA4 y de la LISTA3

lista1 = [1,2,3,"leandro"]
lista2 = [4,5,6,"villalba"]

lista1.append(456789)
lista1.append("Hola mundo")

lista2.append("Hola y adios")
lista2.append(5555)


lista3 = lista1[0:5]
lista4 = lista2[1:3]

print(lista3)
print(lista4)

listas = lista4 + lista3
print(listas)