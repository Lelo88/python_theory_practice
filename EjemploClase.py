expresiones = [not False, not (3 == 5), (33/3 == 11) and (5>2), True or False, 
               (True*5 == 2.5*2) or (123>=3), (12>7) and (True<False) ]

print(expresiones)

nombre = input("Ingrese un nombre: ")
edad = int(input("Ingrese una edad: "))

expresiones = (nombre != "****") and ((edad>5) and (edad<20)) and ((len(nombre) >=4) and ((len(nombre))<8)) and ((edad*3)>35 )
expresiones2 = nombre != "****", (edad>5) and (edad<20), (len(nombre) >=4) and (len(nombre)<8), ((edad*3)>35 )
print(f'La expresion da como resultado el valor booleano: {expresiones}')
print(f'La expresion da como resultado el valor booleano: {expresiones2}')