#Escribir un código que pida al usuario ingresar por teclado:a. Nombreb. Apellidoc. Un pais
# Imprimir por pantalla el mensaje: ‘Hola {nombre} {apellido}, la capital de tu país es {capital}’
# Si el nombre o apellido tienen espacios en blanco al principio o al final, eliminarlos
# El nombre y apellido deben estar capitalizados (primer letra mayúscula y el resto minuscula)

capitales = [("Bolivia", "Sucre"), ("Peru", "Lima"), ("Argentina", "Buenos Aires"),
            ("Chile", "Santiago"), ("Brazil", "Brasilia"), ("Colombia", "Bogotá"),
            ("Mexico", "Mexico DF"), ("Guatemala", "Ciudad de Guatemala"), ("Ecuador", "Quito")]

nombre = input("Nombre: ").capitalize()
apellido = input("Apellido: ").capitalize()
pais = input("Pais: ").capitalize()

while " " in nombre or " " in apellido:
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")

capital = [cap[1] for cap in capitales if pais in cap[0]] #busco en una tupla la capital del pais y lo paso a una tupla
if not capital:
    print("No tenés una capital asignada")
else:    
    print(f'Hola {nombre} {apellido}, la capital de tu pais es {capital[0]}')

#cap=""

#for capital in capitales:
#    if pais in capital[0]:
#        cap = capital[1]
#        break
#    else:
#        cap="No tiene capital"
