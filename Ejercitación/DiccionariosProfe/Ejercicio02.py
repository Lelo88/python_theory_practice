# Escribir un algoritmo que pida al usuario que ingrese nombres (uno a la vez) hasta que el usuario ingrese la palabra ‘fin’ 
# Agregar todos los nombres dentro de una lista ordenados alfabeticamente. Imprimir la lista
# NO SE PERMITE usar el metodo sort

listado = []
palabra = input("Ingrese una palabra distinta a 'fin': ")
while palabra!='fin':
    listado.append(palabra)
    palabra = input("Ingrese una palabra distinta a 'fin': ")
    

for i in range(0,len(listado)):
    for j in range(0, len(listado)):
        if listado[i]<listado[j]:
            aux = listado[i]
            listado[i] = listado[j]
            listado[j] = aux    
    
print(listado)
    