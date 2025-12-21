#Escribí un programa que solicite al usuario ingresar tres números 
# para luego mostrarle el promedio de los tres.

numero1 = int(input("Primer número: "))
numero2 = int(input("Segundo número: "))
numero3 = int(input("Tercer número: "))

promedio = round((numero1 + numero2 + numero3)/3,2) 

print(f'El promedio de los numeros ingresados es: {promedio}') 

