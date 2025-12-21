colores = {"amarillo":"yellow","azul":"blue", "verde":"green"}
print(colores.get("rojo","no hay color rojo"))
print(colores.get("amarillo","no hay color amarillo"))
#La función get sirve para poder buscar un elemento a partir de su key, en el caso de no encontrar 
# devuelve un valor por defecto que le indicamos nosotros. Se escribe como: dict.get(key, “valor por defecto”)

print(colores.keys())
#La función key sirve para poder traer todas las claves de un diccionario en el caso de desconocerlas. 

print(colores.values())
#La función values es similar a keys, pero esta sirve para poder traer todos los valores de un diccionario. 

for clave, valor in colores.items():
    print(clave, valor)
#La función items es similar a keys y values, pero esta crea una lista con clave y valor 
# de los ítems de un diccionario

