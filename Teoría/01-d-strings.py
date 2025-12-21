# Comillas simples

ejemplo_comillas_simples = 'Hola como estas'

# Comillas dobles
ejemplo_comillas_dobles = "hola como estas"

# Cualquiera de las dos es utilizada para colocar caracteres especiales
ejemplo_menciones = 'tu apodo es "Lelo".'


print('Ejemplo de uso de comillas simples: ', ejemplo_comillas_simples)
print('Ejemplo de uso de comillas dobles: ',ejemplo_comillas_dobles)
print('Ejemplo de uso de menciones: ',ejemplo_menciones)

# string multilinea (""" o ''')

ejemplo_string_multilinea = """ Hola como estas 
    espero que bien"""

print('Ejemplo de uso de multilineas: ',ejemplo_string_multilinea)

# caracteres especiales
ejemplo_caracteres_especiales = "Leandro dijo \"Hola como estas\""
print('Ejemplo de uso de caracteres especiales (contrabarra): ',ejemplo_caracteres_especiales)

ejemplo_tabulacion = "Nombre: \t Leandro"
print('Ejemplo de uso de tabulación: ',ejemplo_tabulacion)

ejemplo_salto_de_linea = "Hola como estas \n espero que bien"
print('Ejemplo de salto de línea: ',ejemplo_salto_de_linea)

ejemplo_concatenacion_de_cadenas = ejemplo_comillas_simples + ejemplo_string_multilinea
print('Ejemplo de concatenacion: ', ejemplo_concatenacion_de_cadenas)

nombre = 'Leandro'
apellido = 'Villalba'

nombre_completo = f" {nombre} {apellido}"

print(f'Hola {nombre} {apellido}' )
print(nombre_completo)

# longitud de una cadena
longitud_nombre_completo = len(nombre_completo)
print("longitud de nombre completo: ", longitud_nombre_completo)


#normalizacion de cadenas - upper y lower

print("nombre completo en mayuscula: ", nombre_completo.upper())
print("nombre completo en minuscula: ", nombre_completo.lower())

# Las cadenas son inmutables, no pueden cambiarse sus valores, pero si podemos agregar nuevos valores
animal = 'gato'
# animal[4] = 's'
# forma correcta
plural = animal + 's'
print(plural)

# slicing o manejo de subcadenas
# slice es una "rebanada", en este caso, una porción de una cadena. Esto se puede utilizar para extracciones
# particulares para un determinado proceso.
# sintaxis : texto[iniio : fin: paso]. Podemos trabajar con ìndices positivos y negativos

# normal
porcion_nombre = nombre[0:3:1]
print(f'{porcion_nombre}')

# atajo desde el inicio
porcion_nombre = nombre[:4]
print(f' atajo desde el inciio: {porcion_nombre}')

#atajo hasta el final
porcion_nombre = nombre[3:]
print(f'atajo hasta el final: {porcion_nombre}')

# indices negativos
porcion_nombre = nombre[-4:-1]
print(f'indices negativos: {porcion_nombre}')

porcion_nombre = nombre [::-1]
print(f'nombre al revès: {porcion_nombre}')

# reemplazo de subcadenas
frase = 'Hola como estas'
nueva_frase = frase.replace('estas', 'te va') #reemplaza la subcadena 'estas' por 'te va' y lo guarda en una nueva variable
print(f'frase original: {frase}')
print(f'frase modificada: {nueva_frase}')

# multiplicacion de cadenas
repeticion = 'hola ' * 3
print(f'repeticion de cadena: {repeticion}') #multiplica la cadena 'hola ' por 3 y la guarda en una nueva variable

# busqueda de subcadenas
frase = 'Hola como estas, espero que bien'
posicion = frase.find('espero') #busca la subcadena 'espero'
print(f'posicion de la subcadena "espero": {posicion}') #muestra la posicion donde comienza la subcadena 'espero'

# verificacion de existencia de subcadenas
frase = 'Hola como estas, espero que bien'
existe = 'espero' in frase #verifica si la subcadena 'espero' existe en la cadena frase
print(f'existe la subcadena "espero" en la frase?: {existe}') #muestra True o False dependiendo si existe o no la subcadena