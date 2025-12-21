#Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el 
# nombre tabla-n.txt la tabla de multiplicar de ese número, done n es el número introducido

archivo = open("Ejercitación/Archivos/tabla-n.txt", "w", encoding="utf-8")

numero = int(input("Ingrese un a numero del 1 al 10: "))

while (numero<1) or (numero>10):
    numero = int(input("Ingrese un numero del 1 al 10: "))

for num in range(1,11):
    archivo.write(f'{numero} x {num} = {numero*num}\n')
    
archivo.close()

