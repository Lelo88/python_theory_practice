conjunto = {1,2,3,4}
conjunto2 = conjunto.copy() #copia un conjunto a una variable
print(conjunto2)

conjunto3 = {5,6,7}
print(conjunto.isdisjoint(conjunto3))   #Esta función comprueba si el set es distinto a otro set, es decir, 
                                        #si no hay ningún ítem en común entre ellos. 

conjunto4 = {-1,99}
print(conjunto4.issubset(conjunto)) 
#Esta función comprueba si el set es subset de otro set, es decir, si todos sus ítems están en el otro conjunto.

conjunto5= {5,6}
print(conjunto3.issuperset(conjunto5)) 
#Esta función es muy similar al issubset, la diferencia es que esta comprueba si el set
#es contenedor de otro set, es decir, si contiene todos los ítems de otro set.

print(conjunto.union(conjunto3))
#Esta función une un set con otro, y devuelve el resultado en un nuevo set

print(conjunto.difference(conjunto3))
#Esta función encuentra todos los elementos no comunes entre dos set, 
# es decir, nos devuelve un set de ítems diferentes entre cada set. 

print(conjunto.difference_update(conjunto3))
#Similar al difference, pero esta función nos guarda los ítems distintos en el set originales, 
# es decir, le asigna como nuevo valor los ítems diferentes. 

conjunto6 = {4,5,6}
print(conjunto.intersection(conjunto6))
#Esta función devuelve un set con todos los elementos comunes entre dos set, 
# es decir, nos devuelve un set de ítems iguales entre cada set. 

conjunto.intersection_update(conjunto6)
print(conjunto)
#Es exactamente igual al intersection, pero esta función actualiza el set original, 
# es decir, le asigna como nuevo valor los ítems en común. 