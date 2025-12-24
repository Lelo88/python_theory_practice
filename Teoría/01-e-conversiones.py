# Definimos una variable de tipo string
numero_texto = "123"
print(type(numero_texto))

# Convertimos el string a entero
numero_entero = int(numero_texto)
print(type(numero_entero))
print(numero_entero)
print(numero_entero + 10)

# Convertimos el string a float
numero_float = float(numero_texto)
print(type(numero_float))
print(numero_float)

# Convertimos un número a string
numero = 456
numero_a_texto = str(numero)
print(type(numero_a_texto))
print(numero_a_texto)

# También podemos convertir booleanos
valor_booleano = True
texto_booleano = str(valor_booleano)
print(type(texto_booleano))
print(texto_booleano)

# Convertimos un número decimal a entero
numero_decimal = 4.56
entero_desde_decimal = int(numero_decimal)
print(f"Número decimal: {numero_decimal}")
print(f"Entero convertido: {entero_desde_decimal}")

# Convertimos un número negativo decimal a entero
numero_negativo = -3.7
entero_negativo = int(numero_negativo)
print(f"Número negativo: {numero_negativo}")
print(f"Entero convertido: {entero_negativo}")

# Ejemplo con cadena que no es un número válido
try:
    invalido = "abc"
    int(invalido)
except ValueError as e:
    print(f"Error al convertir '{invalido}' a entero: {e}")
    
# Convertimos string a booleano
texto_bool = "True"
bool_valor = bool(texto_bool)
print(f"String '{texto_bool}' convertido a booleano: {bool_valor}")

# Convertimos string vacío a booleano
vacio = ""
bool_vacio = bool(vacio)
print(f"String vacío convertido a booleano: {bool_vacio}")

# Convertimos número 0 a booleano
cero = 0
bool_cero = bool(cero)
print(f"Número 0 convertido a booleano: {bool_cero}")

# Convertimos número 1 a booleano
uno = 1
bool_uno = bool(uno)
print(f"Número 1 convertido a booleano: {bool_uno}")

# Convertimos número -5 a booleano
menos_cinco = -5
bool_menos_cinco = bool(menos_cinco)
print(f"Número -5 convertido a booleano: {bool_menos_cinco}")

# Resumen de conversiones
print("\n=== RESUMEN DE CONVERSIONES ===")
print(f"String '123' -> Entero: {int('123')}")
print(f"String '123' -> Flotante: {float('123')}")
print(f"Entero 456 -> String: '{str(456)}'")
print(f"Booleano True -> String: '{str(True)}'")
print(f"String 'True' -> Booleano: {bool('True')}")
print(f"String vacío -> Booleano: {bool('')}")
print(f"Número 0 -> Booleano: {bool(0)}")
print(f"Número 1 -> Booleano: {bool(1)}")
print(f"Número -5 -> Booleano: {bool(-5)}")
print("=== FIN DEL RESUMEN ===")