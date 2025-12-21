# Escribí un programa que solicite al usuario el ingreso de dos números diferentes y 
# muestre en pantalla al mayor de los dos.

numero = int(input("Un número: "))
numero2 = int(input("Otro número: "))

if (numero > numero2):
    print(f'{numero} es mayor')
else:
    print(f'{numero2} es mayor')

