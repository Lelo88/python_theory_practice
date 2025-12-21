#se pueden tener distintos tipos de errores en python, pero pueden ser controlados
# a traves del bloque try except

try:
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))
    print(f'{num1/num2}')
except ValueError:
    print("La division no puede realizarse")
    
print("--------------------------------------")

while (True):
    try:  
        a = float(input("Introduce un número: "))
        b = float(input("Introduce otro número: "))
        print(a + b)
    except ValueError:
        print("Ha ocurrido un error. Tienes que introducir 2 números.")
    else:
        print("La suma se ha realizado correctamente.")
        break  # Importante romper la iteración si todo ha ido bien.
        