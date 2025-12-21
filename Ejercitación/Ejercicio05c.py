#Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:
# Si el primer número es mayor que el segundo, debe devolver 1
# Si el primer número es menor que el segundo, debe devolver -1
# Si ambos números son iguales, debe devolver un 0.
# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'

num1=int(input("Ingrese el primer número: ")) #realizamos el ingreso de las variables
num2=int(input("Ingrese el segundo número: "))

def relacion(n1,n2): #colocamos dos parametros para luego realizar sus comparaciones y sus retornos
    if n1>n2:
        return 1
    elif n1<n2:
        return -1
    else:
        return 0
    
print(relacion(num1,num2)) #realizamos el llamado a la funcion colocando como argumentos los numeros ingresados   