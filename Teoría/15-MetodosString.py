cadena = "hola como estas"
cadena2 = "HOLA COMO ESTAS"

print(cadena.upper()) #pone todo en mayúsculas
print("CADENA2: " + cadena2.lower()) #pone todo en minúsculas
print(cadena.capitalize()) # pone la primer letra de la cadena en mayuscula 
print(cadena.title()) #le pone a cada palabra de la cadena una mayúscula
print(cadena.count("o"))#cuenta la cantidad de veces que se repite 
print(cadena.find("como"))#devuelve el valor la ubicacion de la palabra que pasamos como argumento
print(cadena.rfind("como"))#lo mismo que find, pero empezando desde el final

print(cadena.split())#separa las palabras colocandolas dentro de un listado

print(",".join(cadena))#agrega entre caracteres lo que colocamos antes del join
print(cadena.strip("s"))#elimina los caracteres de costado que especifiquemos entre parentesis. por default elimina el espacio
print(cadena.replace("o","x"))#reemplaza el caracter de una cadena por otro
#tambien se pueden agregar palabras 
