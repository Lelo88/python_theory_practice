#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde 
# en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, 
# vive en <dirección> y su número de teléfono es <teléfono>.

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
direccion = input("Ingrese su direccion: ")
telefono = input("Ingrese su telefono: ")

datos = {"Nombre" : nombre, "Edad": edad, "Direccion": direccion, "Telefono": telefono }

print(f'Su nombre es {datos["Nombre"]} y tiene {datos["Edad"]}')
print(f'Vive en {datos["Direccion"]} y su telefono es {datos["Telefono"]}')