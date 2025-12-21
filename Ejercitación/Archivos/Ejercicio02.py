archivo = open("Ejercitación/Archivos/tabla-n.txt", "r", encoding="utf-8")

numero = int(input("Ingrese un numero del 1 al 10: "))
while (numero<1) or (numero>10):
    numero = int(input("Ingrese un numero del 1 al 10: "))
    
if archivo.readline(1) == str(numero):
    print(numero)
else:
    print("El número no es factor de la tabla")
    
archivo.close()