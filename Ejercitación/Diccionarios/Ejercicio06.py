
#Escribir un programa que cree un diccionario simulando una cesta de la compra.
#El programa debe preguntar el artículo y su precio y añadir el par al diccionario,
#hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de
#la compra y el coste total, con el siguiente formato


cesta = {}
pregunta = input("Desea ingresar articulos para comprar? ")

while pregunta=='s':
    articulo = input("Ingrese el nombre del articulo")
    precio = float(input("Ingrese el precio del articulo: "))
    cesta.update({articulo:precio})
    pregunta=input("Desea ingresar mas articulos?: ")

#total = 0
#for art, pre in cesta.items():
    #print(f'{art}  {pre}')
    #total+=pre
print("------------------")
print(f'Total:   {sum(cesta[item] for item in cesta)}') #la forma de mostrar la suma de los valores 

