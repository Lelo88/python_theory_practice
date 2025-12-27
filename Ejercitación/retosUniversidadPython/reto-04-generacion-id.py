from random import randint

nombre = input("Ingrese un nombre: ")
apellido = input("Ingrese un apellido: ")
ano_nacimiento = input("Ingrese un año de nacimiento: ")

primeras_dos_letras_nombre = nombre[:2].upper()
primeras_dos_letras_apellido = apellido[:2].upper()
ultimos_dos_digitos_ano_nacimiento = ano_nacimiento[-2:]

generacion_cuatro_digitos_aleatorios = str(randint(0000, 9999))

print(f'Hola {nombre} {apellido}, tu ID es: {primeras_dos_letras_nombre}{primeras_dos_letras_apellido}{ultimos_dos_digitos_ano_nacimiento}{generacion_cuatro_digitos_aleatorios}')
