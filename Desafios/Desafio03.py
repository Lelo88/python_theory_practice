#mostrar una cadena de texto al revés 

nombre_alumno = "Leandro Villalba"

print(nombre_alumno[2:10])
print(nombre_alumno[::-1])
print(nombre_alumno[1:11:2])

#ingresar una nota y el nombre de la materia y mostrarla por consola

nota = int(input("Ingrese una nota: "))
materia = input("Ingrese la materia correspondiente a la nota")

print(f'El alumno {nombre_alumno} sacó un {nota} en la materia {materia}')