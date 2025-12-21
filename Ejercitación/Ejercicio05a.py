#Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y una altura. 
# Calcula el área de un rectángulo de 15 de base y 10 de altura 

import os

os.system("cls")
bas=input("Ingrese el tamaño de la base: ")
alt = input("Ingrese el tamaño de la altura: ")

def area_rectangulo(base,altura):
    while not(base.isnumeric() and altura.isnumeric()):
        os.system("cls")
        base=input("Ingrese el tamaño de la base: ")
        altura=input("Ingrese una altura: ")
    base = int(base)
    altura=int(altura)
    return f'Área del rectángulo: {base} x {altura} = {base*altura}'

print(area_rectangulo(bas,alt))
