# con la comprension de listas podemos realizar diversas soperaciones con los listados que estemos trabajando

usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Juan", 3],
]

#nombres = []

#for usuario in usuarios:
#    nombres.append(usuario[0])
    
#print(nombres)

# hay una forma mucho mas facil de resolver el paso anterior

nombres = [usuario[0] for usuario in usuarios] # elemento del listado para un elemento en listado
print(nombres)

# tambien podemos realizar un filtrado en base a alguna condición
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres)

#lo mismo que hace dos pasos atras podemos implementar con la funcion map

nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)

#podemos realizar el filtrado
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)