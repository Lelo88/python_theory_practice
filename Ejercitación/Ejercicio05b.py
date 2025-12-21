#Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. 
# Calcula el área de un círculo de 5 de radio
# 🖐Ayuda: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado 
# por el número pi. Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math.

import math

rad = int(input("ingrese el radio del circulo: "))

def area_circulo(radio):
    return f' Area del circulo = {radio}² x {round(math.pi,4)} = {round(pow(int(radio),2)*(math.pi),2)}'

print(area_circulo(rad))