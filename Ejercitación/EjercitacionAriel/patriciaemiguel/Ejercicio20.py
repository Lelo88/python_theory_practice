# Escribí un programa para solicitar al usuario tres números y mostrar en pantalla 
# al menor de los tres.

num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Tercer número: "))

if (num1<num2)and(num1<num3):
    print(f'El numero {num1} es el menor')
elif(num2<num1) and (num2<num3):
    print(f'El numero {num2} es menor')
else:
    print(f'El numero {num3} es menor')
