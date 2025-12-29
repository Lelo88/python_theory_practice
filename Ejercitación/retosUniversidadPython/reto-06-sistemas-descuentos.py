# Sistema de descuentos (ejemplo de operador and)

CANTIDAD_PRODUCTOS_DESCUENTO = 10
cantidad_productos = int(input("Ingrese la cantidad de productos: "))
tiene_membresia = input("Tiene membresia? (si/no): ")

es_elegible_descuento = (cantidad_productos >= CANTIDAD_PRODUCTOS_DESCUENTO
                         and tiene_membresia.strip().lower() == "si")

print(f'¿Tiene acceso al descuento? {es_elegible_descuento}')