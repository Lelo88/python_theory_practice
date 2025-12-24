# Ejemplo de uso de input en Python

nombre = input("¿Cuál es tu nombre? ")
print(f"Hola, {nombre}!")

edad = int(input("¿Cuántos años tienes? "))
print(f"Tienes {edad} años.")

# Ejemplo con manejo de errores
try:
    temperatura = float(input("Ingresa la temperatura en Celsius: "))
    print(f"La temperatura es {temperatura}°C")
except ValueError:
    print("Por favor ingresa un número válido.")

# Ejemplo de input en un bucle
while True:
    respuesta = input("¿Quieres continuar? (s/n): ")
    if respuesta.lower() == 'n':
        break
    elif respuesta.lower() == 's':
        print("Continuando...")
    else:
        print("Por favor responde 's' o 'n'.")
        
print("Programa finalizado.")
print("¡Hasta luego!")
print("Gracias por usar el programa.")

# Ejemplo del curso universidad de python.

print('*** Sistema de empleados ***')
nombre_empleado = input('Nombre del empleado: ')
print(f'Nombre: {nombre_empleado}')
edad_empleado = int(input('Edad del empleado: '))
print(f'Edad: {edad_empleado}')
salario_empleado = float(input('Salario del empleado: '))
print(f'Salario: {salario_empleado}')
esta_contratado = input('¿Está contratado? (s/n): ').lower() == 's'
print(f'Contratado: {esta_contratado}')

# Ejemplo de input con validación avanzada
def obtener_numero_valido(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor ingresa un número válido.")

numero = obtener_numero_valido("Ingresa un número: ")
print(f"El número ingresado es: {numero}")