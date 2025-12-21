letras = ['a','b','c']
letras.clear() #limpia todo lo que se encuentra dentro del listado
print(letras)

numeros = [1,2,3,4]
numeros.extend([5,6,7,8]) #extiende un listado con el parametros que agreguemos
print(numeros)

numeros.insert(0,0)#Esta función integrada se usa para agregar un ítem a una lista, pero en un índice específico. 
print(numeros)
numeros.reverse()#da vuelta una lista. no lo puedo poner dentro de un print porque me devuelve none
print(numeros)

numeros2 = [10,1,-5,8,-20,3,4]
numeros2.sort() #me devuelve una lista ordenada de menor a mayor
print(numeros2) 

numeros2.sort(reverse=True) #la inversa de sort
print(numeros2)

#--------------------------------------
#podemos tener los siguientes listados en una lista

usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Juan", 3],	
]

def ordenarUsuarios(usuarios1):
    return usuarios1[1]

usuarios.sort(key=ordenarUsuarios) #pasamos la referencia ordenar usuarios, ya que sort la hace
print(usuarios)

#--------------------------------
#funciones lambda

usuarios.sort(key=lambda x: x[1], reverse=True)
print(usuarios)