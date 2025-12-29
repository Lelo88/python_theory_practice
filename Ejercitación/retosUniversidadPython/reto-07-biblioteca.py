# Sistema de biblioteca (ejemplo de operador or)

DISTANCIA_PERMITIDA_KM  = 3
tiene_credencial = input("Tiene credencial? (Si/No): ")
distancia_km = int(input("¿A cuantos kilometros vives de la biblioteca?: "))

es_elegible = (tiene_credencial.strip().lower() == "si"
               or distancia_km <= DISTANCIA_PERMITIDA_KM)

print(f'¿Tiene acceso a la biblioteca? {es_elegible}')