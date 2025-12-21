#Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
# Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, 
# y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, 
# correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. 
#El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, 
# (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, 
# (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida 
# el programa tendrá que hacer lo siguiente: 
# Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
# Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
# Preguntar por el NIF del cliente y mostrar sus datos.
# Mostrar lista de todos los clientes de la base datos con su NIF y nombre
# Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
# Terminar el programa.

import os

cliente = {}
titulo = "-----BASE DE DATOS DE CLIENTES-----"
opcion=0

while opcion!=6:
    os.system("cls")
    print(titulo.center(130))
    print("•MENU DE OPCIONES•\n")
    print("1- Añadir clientes")
    print("2- Eliminar clientes")
    print("3- Modificar clientes")
    print("4-  clientes")
    print("5- Listar clientes preferentes")
    print("6- Terminar")
    opcion = int(input("\n Elija una opción:"))
    
    os.system("cls")
    if opcion == 1:
        dni = int(input("Ingrese el ID del cliente: "))
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        email = input("Correo electrónico: ")
        preferencia = input("Cliente preferente").upper() 
        datos = ({"Nombre": nombre, "Apellido": apellido, 
        "Direccion": direccion,"Telefono": telefono,"E-mail":email, "Preferente": preferencia})
        cliente[dni] = datos
        os.system("pause")
    elif opcion == 2:
        idCliente = int(input("Cliente que desea sacar de la base de datos (DNI): "))
        if (idCliente in cliente):
            cliente.pop(idCliente)
            print("Cliente eliminado\n")
        else: 
            print("El cliente no se encuentra dentro de la base de datos\n")
        os.system("pause")
    elif opcion == 3:
        idCliente = int(input("Ingrese el DNI del cliente que desea ver: "))
        if idCliente in cliente:
            for detalle,valor in cliente.items():
                print(detalle,valor)
        else:
            print("El DNI ingresado no se encuentra en la base de datos")
        os.system("pause")
    elif opcion == 4: 
        for dni, valor in cliente.items():
            print(f'{dni}:{valor["Nombre"]} {valor["Apellido"]}')
        os.system("pause")
    elif opcion == 5:
        for clave,valor in cliente.items():
            if valor["Preferente"] =='S':
                print(f'{clave}: {valor["Nombre"]} {valor["Apellido"]}')
        os.system("pause")
    elif opcion == 6:
        print("Usted está saliendo de la base de datos. Hasta pronto.")
    else:
        print("La opción ingresada es incorrecta")             
        
#Aspectos a mejorar: Ingreso de clientes, muestra de datos, pedido de eliminacion de datos