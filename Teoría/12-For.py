lista = [0,1,2,3,4,5,6,7,8,9,10]
for num in lista: #num es una variable creada del objeto que se esta iterando
    print('Soy un valor de la lista y valgo', num)
    num *= 5 #con esa variable creada en el bucle la utilizo para modificar la lista
    print('Soy un valor de la lista y ahora valgo', num)

print("-----------------------------")
#Ejemplo 2

indice = 0
numeros = [0,1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    numeros[indice] *= 5
    indice += 1
print(numeros)		


print(list(enumerate(numeros, start = 0))) # imprime el indice y el valor de la lista. Lo tengo que poner asi
                                           #porque poniendo enumerate solo me da la posicion de memori

#Si quisiéramos recorrer un string:

texto = 'Hola Mundo, estoy usando for en Python'
for letra in texto:
    print(letra)
texto2 = ''
for letra in texto:
    texto2 = letra * 2
print(texto2)

#Igual que en la sentencia while podemos usar un else al final de la iteración.


for numero in range(10):
    print('Numero vale',numero)
else:
    print("Se terminó de iterar y numero vale: ", numero)

for numero in range(10):
    if numero == 2:
        continue
    elif numero == 8:
        break
    else:
        print("Se terminó de iterar y numero vale: ", numero)

#agregamos una for-else mas para mostrar mejor el ejemplo

numero2 = 10

for num in range(5):
    print(num)
    if num == numero2:
        print("encontrado", numero2)
        break
else:
    print("no encontrado")
    
    
