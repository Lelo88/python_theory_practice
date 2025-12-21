mascotas = ['perro', 'gato', 'pulga', 'wolfgang']

for mascota in mascotas:
    #imprimimos cada mascota del listado mascotas
    print(mascota)
    
for mascota in enumerate(mascotas):
    #nos devuelve tuplas si agregamos el enumerate
    print(mascota) 
    
for mascota in enumerate(mascotas):
    #nos devuelve el valor de mascotas obtenido de una tupla
    print(mascota[1])
    
for indice, mascota in enumerate(mascotas):
    #de esta manera podremos imprimir por separado
    print(indice + 1 )
    print(mascota)    
    
    