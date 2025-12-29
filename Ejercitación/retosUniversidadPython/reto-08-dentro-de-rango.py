# Sistema de rango (ejemplo de operador not)

dato = int(input("Ingrese un numero: "))

es_elegible = not (dato < 0 or dato > 10)
print(f'¿El numero esta dentro del rango [0, 10]? {es_elegible}')

