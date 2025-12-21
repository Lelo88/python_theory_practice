# Escribí un programa que pida al usuario un número entero del 0 al 9, y que mientras el número 
# no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra 
# en la lista de números y notificarlo:

numeros = [1,3,6,9]
numero = int(input("Ingrese un numero del 0 al 9: "))

while (numero<0) or (numero>9):
    numero = int(input("Ingreso incorrecto. Vuelva a intentarlo: "))

if(numero in numeros):
    print("El numero ingresado se encuentra en el listado.")
else:
    print("El numero ingresado no se encuentra en el listado.")    