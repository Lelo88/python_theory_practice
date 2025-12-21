#4) Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio:
# Ayuda: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2
# Comprueba el punto intermedio entre -12 y 24

num1=int(input("Ingrese un número: ")) #realizamos el ingreso de los numeros 
num2=int(input("Ingrese otro número: "))

def intermedio(n1,n2): #colocamos dos parametros, con los que realizaremos la media
    return print(f'El punto intermedio de los numeros ingresados es: {round((n1+n2)/2,1)}') 

intermedio(num1,num2) #realizamos el llamado a la funcion con los numeros ingresados