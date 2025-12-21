#Idem ejercicio #2 pero ordenar la lista en función de la longitud de los nombres, de menor a mayor 
# SI SE PERMITE sort pero no es obligatorio

listado = []
palabra = input("Ingrese una palabra distinta a 'fin': ")
while palabra!='fin':
    listado.append()
    listado.sort(key=len,reverse=True)#permite ordenar las palabras por tamaño debido al key que es el tamaño de cada palabra
    palabra = input("Ingrese una palabra distinta a 'fin': ")

print(listado)
