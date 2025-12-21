from pprint import pprint

# 01. Retornar por medio de una lista de comprension una cadena de caracteres sin espacios en blanco

string = "Hola esta es una cadena de texto"

def quita_espacios(texto):
    return [char for char in texto if char != ' ']

sin_espacios = quita_espacios(string)
print(sin_espacios)

# 02 Contar en un diccionario cuantas veces se repite una letra en un string
def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

contados = cuenta_caracteres(sin_espacios)
pprint(contados, width=1)

#03

def ordena(dict):
    return sorted(
        dict.items(),
         key= lambda key: key[1],
         reverse=True
    )
# la funcion recibe como parametro un diccionario y me devuelve una lista de tuplas con la cantidad de caracteres 
# ordenados de forma descendente    
ordenados = ordena(contados)
print(ordenados)   

# 04 
def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta [orden[0]] = orden[1]
    return respuesta

mayores = mayores_tuplas(ordenados)
print(mayores)

#05 crear un formato de mensaje que permita ver los caracteres que mas se repitieron

def crea_mensaje(diccionario):
    mensaje = "Los que mas se repiten son: \n"
    for clave,valor in diccionario.items():
        mensaje += f"{clave} - {valor}\n"
    return mensaje
            
print(crea_mensaje(mayores))
