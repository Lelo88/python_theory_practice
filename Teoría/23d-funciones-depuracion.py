def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado

print("Antes del llamado a la función")
large = largo("Hola")
print(large)

""" Check if the given text is a palindrome.
Parameters:
- texto (str): The text to be checked.
Returns:
- bool: True if the text is a palindrome, False otherwise.
"""


def es_palindromo(texto):
    resultado = True
    for i in range(0, len(texto)//2):
        if texto[i] != texto[len(texto)-i-1]:
            resultado = False
    return resultado

print(es_palindromo("hola"))

def es_palindromo2(texto):
    textoSinEspacios = texto.replace(" ", "").lower()
    return textoSinEspacios == textoSinEspacios[::-1]

print(es_palindromo2("hola"))
print(es_palindromo2("amo la paloma"))
print(es_palindromo2("Amo la paloma"))