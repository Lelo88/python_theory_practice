persona = {"nombre": None,
           "apellido": None,
           "Edad": None}

#persona["nombre"] = input("Nombre: ")
#persona["apellido"] = input("Apellido: ")
#persona["Edad"] = int(input("Edad: "))

#de esta forma reduzco el codigo de arriba
for dato in persona.keys():
    persona[dato] = input(f'{dato}: ')
    
print(persona)

archivo = open("Teoría/ArchivoEjemplo19.txt","a",encoding="utf-8")


for dato in persona.values():
    archivo.write(dato + " ")

archivo.write('\n')

archivo.close()

