#Escribir un algoritmo que pida al usuario que ingrese un mensaje e imprimir por pantalla la cantidad de 
# palabras que componenen el mensaje

frase = input("Ingrese una frase cualquiera: ")
frase=frase.split() #dejando el split de esta manera predeterminada me va a contar absolutamente todos los espacios
print(f'La cantidad de palabras que contiene la frase es {len(frase)}')



