#Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:
# Todos los números del 0 al 10 [0, 1, 2, ..., 10]
# Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
# Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
# Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
# Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
""" 
lista=[[],[],[],[],[]]

for num in range(0,11):
    lista[0].append(num)

for num in range(-10,1):
    lista[1].append(num)

for num in range(0,21,2):
    lista[2].append(num)
    
for num in range(-19,0,2):
    lista[3].append(num)
    
for num in range(0,51,5):
    lista[4].append(num)    

for i in range(0,len(lista)):
    if (i==0):
        print(f'Números creados del 1 al 10: {lista[i]}')
    elif(i==1):
        print(f'Números creados del -10 al 0: {lista[i]}')
    elif(i==2):
        print(f'Números pares del 0 al 20: {lista[i]}')
    elif(i==3):
        print(f'Números impares del -20 a 0: {lista[i]}')
    else:
        print(f'Números múltiples de 5 del 0 al 50 : {lista[i]}') """                    
        
""" lista = [[],[],[],[],[]] #inicializo una lista vacia con 5 listas anidadas para agregar lo solicitado

for i in range(0,len(lista)):
    if i==0:
        for num in range(0,11): #Agrego 11 asi la funcion range me toma el numero 10
            lista[i].append(num) #En el primer indice agrego los numeros del 1 al 10.
        print(f'Números creados del 1 al 10: {lista[i]}')    
    elif(i==1):
        for num in range(-10,1):
            lista[i].append(num)
        print(f'Números creados del -10 al 0: {lista[i]}')        
    elif(i==2):
        for num in range(0,21,2):
            lista[i].append(num)
        print(f'Números pares del 0 al 20: {lista[i]}')    
    elif(i==3):
        for num in range(-19,0,2):
            lista[i].append(num)
        print(f'Números impares del -20 a 0: {lista[i]}')    
    else:    
        for num in range(0,51,5):
            lista[i].append(num)
        print(f'Números múltiples de 5 del 0 al 50 : {lista[i]}')  """
        
lista = [[],[],[],[],[]]

for i in range(0,len(lista)):
    if i==0:
        lista[i]=list(range(0,11))
        print(f'Números creados del 1 al 10: {lista[i]}')    
    elif(i==1):
        lista[i]=list(range(-10,1))
        print(f'Números creados del -10 al 0: {lista[i]}')        
    elif(i==2):
        lista[i]=list(range(0,21,2))
        print(f'Números pares del 0 al 20: {lista[i]}')    
    elif(i==3):
        lista[i]=list(range(-19,0,2))
        print(f'Números impares del -20 a 0: {lista[i]}')    
    else:    
        lista[i]=list(range(0,51,5))
        print(f'Números múltiples de 5 del 0 al 50 : {lista[i]}')    
