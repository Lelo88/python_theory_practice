from collections import deque

# al tener una lista, podemos indicar se cumple el sistema fifop

lista = [1,2,3,4]

# el problema se dan con listas con grandes numeros, teniendo impacto en el rendimiento de la aplicacion 
# con la cual estamos trabajando

fila = deque([1,2])
fila.append(3)
fila.append(4)
print(fila)