#Dentro de las sentencias condicionales el if (si) posiblemente sea la más famosa y utilizada
# en la programación, esto debido a que nos permite controlar el flujo del programa y dividir
# la ejecución en diferentes caminos.
#Al utilizar esta palabra reservada if le estamos indicando a Python que queremos ejecutar
# una porción de código, o bloque de código, solo si se se cumple una determinada condición
# es decir, si el resultado es True.


if (5<10):
    print("5 es menor a 10")
else:
    print("5 es mayor")
    
a = 5
b = 10

if (a>b):print("a es mayor")
elif(b>a): print("b es mayor")
else: print("Los numeros son iguales")

# tambien podemos escribirlos con operadores ternarios

edad = 18
mensaje = "Es mayor de edad" if edad>=18 else "Es menor de edad"
print(mensaje)