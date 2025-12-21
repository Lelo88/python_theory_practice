#Escribí un programa que sume todos los números enteros impares desde el 0 hasta el 100:

sumOdd=0
for num in range(1,100,2):
    sumOdd+=num

print(f'La suma total de todos los impares entre 1 y 100 es de {sumOdd}')