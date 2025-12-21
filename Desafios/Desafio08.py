#Calcular la suma de una cantidad de números enteros ingresados por el usuario 
# directamente utilizando la función input (). 
# Para finalizar la ejecución del programa, el usuario debe escribir la palabra exit(). 
# El programa debe validar dicha acción. 
# Finalmente, el algoritmo debe mostrar la suma parcial y total obtenida.


numeros = (int((input("Ingrese un numero"))))
sumaNum = 0
while(numeros!=0):
    sumaNum += numeros
    numeros = (int((input("Ingrese un numero"))))
    
    
print(f'La suma de los numeros ingresados es: {sumaNum}')