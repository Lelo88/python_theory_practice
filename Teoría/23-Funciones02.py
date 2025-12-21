def saluda(nombre, apellido):
    return f'Hola, mi nombre es {nombre} {apellido} '

#si no invoco nada, nada va a pasar nada, porque estoy retornando un valor

saluda("Leandro","Villalba") # si invoco la funcion con los parametros no va a pasar nada,

print(saluda("Leandro","Villalba"))

def hola (nombre, apellido = "Villalba"):
    return f'hola, mi nombre es {nombre} {apellido} '

hola("Gonzalo") # si invoco la funcion con un parametro, me va a agregar el apellido que se encuentra con default

print(hola("Gonzalo"))

print(hola(apellido="Alvarez", nombre="Gonzalo")) # tambien puedo definir a los argumentos de esta manera



