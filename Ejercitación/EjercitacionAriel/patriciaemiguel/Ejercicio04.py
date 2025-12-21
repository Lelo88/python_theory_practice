#Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por una motocicleta y la cantidad de litros de combustible que consumió durante ese recorrido. 
# Mostrar el consumo de combustible por kilómetro.

kilometros = int(input("Kilometros recorridos: "))
litros = float(input("Litros de combustible gastados: "))

print(f'El consumo por kilometro es de {round(kilometros/litros,2)}')

