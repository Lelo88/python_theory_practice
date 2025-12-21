#manipulando listas

mascotas = ['perro', 'gato', 'pulga', 'wolfgang']
print(mascotas[0])

# puedo cambiar el elemento de una lista
mascotas[0] = 'bicho'
print(mascotas[0])

#me imprime desde el tercer elemento hasta el final
print(mascotas[2:])

#me imprime desde el ultimo elemento
print(mascotas[-1])

# me imprime de dos en dos
print(mascotas[1::2])

numeros = list(range(21))
print(numeros)

print(numeros[1::2])

#------------------------------------------------------------------

#desempaquetado de numeros

otrosnumeros = [1,2,3,4,5]
primer, segundo, *otros = otrosnumeros
print(primer, segundo, *otros)

