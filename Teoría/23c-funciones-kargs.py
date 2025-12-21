def get_products(**datos):
    print(datos)
    
get_products(id = 1 ,nombre="Leandro", apellido="Villalba")
# cuando llamamos a una funcion y en el parametro tiene dos asteriscos, tenemos que pasar en los argumentos
# el nombre y el valor de la variable. esto nos va a retornar un dato de tipo diccionario

def get_products01(**datos):
    print(datos["id"], datos["nombre"])
    
get_products01(id = 1 ,nombre="Leandro", apellido="Villalba")

# no solamente nos puede devolver un diccionario como resultado, sino que tambien podemos
# el valor de cualquiera de los elementos del diccionario que especifiquemos

