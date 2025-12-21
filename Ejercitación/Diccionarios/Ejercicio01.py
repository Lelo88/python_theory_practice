#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa 
# no está en el diccionario.

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda=input("Escriba la moneda que quiera saber: ")

if moneda in monedas:
    print(monedas[moneda]) #entre corchetes pongo la divisa ingresada porque es un string
else:
    print("La divisa no se encuentra.")

#Forma mas rapida de hacerla: 
moneda2 = input("Escriba la divisa: ")
print(monedas.get(moneda2, "No se encuentra la moneda"))

