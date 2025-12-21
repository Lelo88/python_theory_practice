#Escribí un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, 
# debe repetirse el proceso hasta que lo introduzca correctamente.

isOdd=int(input("Ingrese un numero impar: "))
while(isOdd%2==0):
    isOdd=int(input(f'{isOdd} no es impar. Vuelva a ingresar un número impar: '))
else:
    print(f'El número {isOdd} es impar. ¡Muchas gracias!')