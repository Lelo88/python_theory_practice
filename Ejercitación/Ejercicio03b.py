# Crear un bucle que sume los nros impares del 0 al 50

sumaImp = 0  # variable acumuladora de las sumas impares
for num in range(0, 51):
    if num % 2 != 0:  # Pregunto si el numero da un resto distinto de cero
        sumaImp += num  # sumo ese numero dentro del rango a la variable sumaImp para que se acumule y siga sumando

print(f'La suma de todos los impares del 0 al 50 es de {sumaImp}')
