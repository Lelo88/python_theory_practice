#puede haber anidación con listas y tuplas 
listaTupla = [1,3,2,(4,5,6)]
tuplaLista = (7,8,9,[10,11,12])

#acceso a datos anidados
a = [1,2,3]
b = [4,5,6] 
c = [7,8,9]
resultado = [a,b,c]

print(resultado)
print(resultado[0])
print(resultado[0][1])