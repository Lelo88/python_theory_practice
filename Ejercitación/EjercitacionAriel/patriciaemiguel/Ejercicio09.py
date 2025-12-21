#Escribí un programa que solicite al usuario el ingreso de un texto y almacene ese texto en
# una variable. A continuación, mostrar en pantalla la primera letra del texto ingresado.
# Luego, solicitar al usuario que ingrese un número positivo menor a la cantidad de caracteres
# que tiene el texto que ingresó (por ejemplo, si escribió la palabra “HOLA”, tendrá que
# ser un número entre 0 y 4) y almacenar este número en una variable llamada indice.
# Mostrar en pantalla el carácter del texto ubicado en la posición dada por indice.

oracion = input("Ingresa un texto: ")
print(f'El carácter ingresado en primer lugar es {oracion[0]}')
numero = int(input(f'Ingresa un numero positivo menor a {len(oracion)}: '))
print(f'El carácter en esa posición es: {oracion[numero]}')

