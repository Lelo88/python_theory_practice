# Escribí un programa que solicite al usuario un número y le reste el 15%, 
# almacenando todo en una única variable. A continuación, mostrar el resultado final en pantalla.

numero = int(input("Ingresa un número: ")) 
numero -= ((numero*15)/100)

print(f'Descontando el 15 % queda {round(numero,2)}')

