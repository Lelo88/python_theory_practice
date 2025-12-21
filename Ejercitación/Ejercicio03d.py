#1) Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:
# Mostrar una suma de los dos números
#Mostrar una resta de los dos números (el primero menos el segundo)
#Mostrar una multiplicación de los dos números
#Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
#En caso de no introducir una opción válida, el programa informará de que no es correcta.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el primer numero: "))

opcion=0

while(opcion!=4):
    print("1- Suma de los numeros ingresados")
    print("2- Resta de los numeros ingresados")
    print("3- Multiplicacion de los numeros ingresados")
    print("4- Salida del programa")
    opcion= int(input("Ingrese una opcion: "))
    if(opcion==1):
        print(f'La suma de los numeros ingresados es {num1 + num2}')
    elif(opcion==2):
        print(f'La resta de los numeros ingresados es {num1 - num2}')
        continue
    elif(opcion==3):
        print(f'La multiplicacion de los numeros ingresados es {num1 * num2}')
        continue
    elif(opcion==4):
        print('Usted esta saliendo del programa. Hasta pronto!')
        salir=True
    else:
        print('La opcion ingresada no es valida.')                