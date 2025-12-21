#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio 
# de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un 
# mensaje informando de ello.

frutas = {'Platano': 1.35, 'Manzana': 0.8, 'Pera': 0.85, 'Naranja': 0.7}

fruta = input("Que fruta desea comprar?: ")
kilos = int(input("Cuantos kilos?: "))

if fruta in frutas:
    precio = frutas[fruta] * kilos
    print(f'Usted tiene que pagar: {precio}')
else: 
    print("No tenemos esa fruta!")

