limit = int(input("Ingrese la cantidad de numeros que desea ingresar: ")) #pido la cantidad de numeros a ingresar
num_list = [] #incializo una lista vacia

print("Ingrese los numeros a ordenar: ") #en este bucle pido los numeros a ingresar para guardarlos en num_list
for num in range(0,limit):
    num = int(input())
    num_list.append(num)
    
def separar(list_num): #coloco como parametro una variable que representara a la lista 
    list_pair = [] #inicializo dos listas que agregara por un lado a los pares y por otro a los impares
    list_odd = []

    for i in list_num: #recorro la lista ingresada, corroborando sus numeros pares e impares, añadiendolos a las listas correspondientes
        if i % 2 == 0: 
            list_pair.append(i)
            list_pair.sort() #los ordeno a medida que los voy ingresando
        else: 
            list_odd.append(i)
            list_odd.sort()

    return print(f'Lista de pares ingresados: {list_pair} \n Lista de impares ingresados: {list_odd}') 

separar(num_list) #llamo a la funcion con la lista ingresada
