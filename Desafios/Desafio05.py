#Descripción de la actividad. 
# A partir de una variable llamada tupla, imprimir por pantalla de forma ordenada, lo siguiente:
# 1. El último ítem de tupla
# 2. El número de ítems de tupla
# 3. La posición donde se encuentra el ítem 87 de tupla
# 4. Una lista con los últimos tres ítems de tupla
# 5. Un ítem que haya en la posición 8 de tupla
# 6. El número de veces que el ítem 7 aparece en tupla
# Copia esta tupla para iniciar el ejercicio:
# tupla = (8, 15, 4, 39, 5, 89, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

tupla = (8, 15, 4, 39, 5, 89, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

#ultimo item de la tupla
print(tupla[-1]) 

#cantidad de items en la tupla
print(len(tupla))

#la posicion donde se encuentra el item 87 de la tupla
#print(tupla.index(87)) #ValueError: tuple.index(x): x not in tuple

#lista con los tres ultimos de la tupla
listaTupla = list(tupla[-3:]) #o tambien tupla[13:0]

print(listaTupla)



#un item que haya en la posicion 8 de la tupla