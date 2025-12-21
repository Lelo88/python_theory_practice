nombre_curso = "Python"
descripcion_curso = """Curso de Python
Este curso completa todos los detalles que necesitas aprender para encontrar trabajo
como programador
"""

print(nombre_curso, descripcion_curso)

print(len(nombre_curso))
# utilizamos la funcion .upper() y el primer elemento
print(nombre_curso[0].upper())

print(descripcion_curso[0:5])

# FORMATO DE STRINGS

nombre = "Leandro"
apellido = "Gonzalez"

nombre_completo = f"Hola, mi nombre es {nombre} {apellido}"

print(nombre_completo)

# METODOS STRING

animal = "chanchito feliz"
print(animal.upper())  # pasa todo a mayúsculas
print(animal.lower())  # pasa todo a minúsculas
print(animal.capitalize())  # pone la primera letra de la cadena en mayuscula
print(animal.title())  # le pone a cada palabra de la cadena una mayúscula
# cuenta la cantidad de veces que se repite el caracter
print(animal.count("a"))
# devuelve el valor la ubicación de la palabra que pasamos como argumento
print(animal.find("a"))
print(animal.rfind("a"))  # lo mismo que find, pero empezando desde el final
print(animal.split())  # separa las palabras colocandolas dentro de un listado
# elimina los caracteres de costado que especifiquemos entre parentesis. por default elimina el espacio
print(animal.strip("s"))
print(animal.replace("a", "x"))  # reemplaza el caracter de una cadena por otro
nombre_curso = "Python"
descripcion_curso = """Curso de Python
Este curso completa todos los detalles que necesitas aprender para encontrar trabajo
como programador
"""

print(nombre_curso, descripcion_curso)

print(len(nombre_curso))
#utilizamos la funcion .upper() y el primer elemento
print(nombre_curso[0].upper())

print(descripcion_curso[0:5])
print("nCH" in animal) # devuelve un booleano que indica si un elemento se encuentra en un string