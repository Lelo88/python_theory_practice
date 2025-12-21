#Escribí un programa que pida al usuario cuantos números quiere introducir. 
# Luego lee todos los números y realiza una media aritmética:

ingreso = int(input("¿Cuantos numeros desea ingresar?: "))
lista = []
for num in range(0,ingreso):
    num=int(input(f'Ingrese el numero {num + 1}: '))
    lista.append(num)
    
print(f'La media de los numeros ingresados es de {round((sum(lista)/ingreso),2)}')    