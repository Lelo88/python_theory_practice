d = [1,2,3]
e=(4,5,6)
print(d+d)

print(e[1])
print(e + (7,8,9))

numero_1 = 9
numero_2 = 3
numero_3 = 6

media = (numero_1 + numero_2 + numero_3) / 3 #calcula la media de las variables 
print("La nota media es", media)

nota_1 = int(input("Ingrese la primera nota: ")) * 0.15 #realizo el porcentaje de la nota ingresada de manera directa
nota_2 = int(input("Ingrese la segunda nota: ")) * 0.35
nota_3 = int(input("Ingrese la tercera nota: ")) * 0.5

notaFinal = round(nota_1 + nota_2 + nota_3,2) #redondeamos la nota final a un float con dos digitos
                                              #luego de la coma
print(f'La nota final es de {notaFinal}')

matriz = [ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]

matriz[0].append(sum(matriz[0])) #a cada fila de la matriz le agrego a lo ultimo la suma de los elementos la lista anidada definidos anteriormente
matriz[1].append(sum(matriz[1]))
matriz[2].append(sum(matriz[2]))
matriz[3].append(sum(matriz[3]))

print(matriz) #la variable matriz se mostrará con los elementos agregados a cada lista anidada equivalente a la suma
              #de los elementos definidos anteriormente

