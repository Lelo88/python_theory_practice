# ejemplos de pilas = historial de navegacion 

# simplemente es trabajar con listas bajo la logica de pilas

pila = []
pila.append(1)
pila.append(2)
pila.append(3)

print(pila)
ultimoElemento = pila.pop()
print(ultimoElemento)
print(pila)
print(pila[-1])
#aca elimino el resto de los elementos
pila.pop()
pila.pop()

if not pila:
    print("pila vacia")