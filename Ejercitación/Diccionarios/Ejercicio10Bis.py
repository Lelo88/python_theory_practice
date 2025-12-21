import os

cliente = {}
titulo = "-----BASE DE DATOS DE CLIENTES-----"
opcion=0

while opcion!=6: #inicio del menu
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

        while dni!=0: #mientras el dni sea distinto de 0
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            email = input("Correo electrónico: ")
            preferencia = input("Cliente preferente: ").upper() 
            datos = ({"Nombre": nombre, "Apellido": apellido, 
            "Direccion": direccion,"Telefono": telefono,"E-mail":email, "Preferente": preferencia})
            #ingreso todos los datos en el diccionario datos
            cliente[dni] = datos #por cada clave dni generada coloco los datos ingresados del diccionario datos
            datos = len(datos) + 1 #aumento en uno la cantidad de elementos en datos para almacenar nuevos datos si ingreso otro dni
            dni = int(input("Ingrese el ID del cliente: "))
        os.system("pause")
    elif opcion == 2:
        idCliente = int(input("Cliente que desea sacar de la base de datos (DNI): "))
        if (idCliente in cliente):
            cliente.pop(idCliente) #elimino al cliente que coloco en la busqueda
            print("Cliente eliminado\n")
        else: 
            print("El cliente no se encuentra dentro de la base de datos\n")
        os.system("pause")
    elif opcion == 3:
        idCliente = int(input("Ingrese el DNI del cliente que desea ver: "))
        if idCliente in cliente: #muestro al cliente que busco con los datos correspondientes
            for detalle,valor in cliente.items(): 
                print(f'{detalle}:{valor["Nombre"]} {valor["Apellido"]}')
        else:
            print("El DNI ingresado no se encuentra en la base de datos")
        os.system("pause")
    elif opcion == 4: 
        for dni, valor in cliente.items(): #muestro a todos los clientes
            print(f'{dni}:{valor["Nombre"]} {valor["Apellido"]}') 
        os.system("pause")
    elif opcion == 5:
        for clave,valor in cliente.items():
            if valor["Preferente"] =='S': #muestro a los clientes que sean preferentes
                print(f'{clave}: {valor["Nombre"]} {valor["Apellido"]}')
        os.system("pause")
    elif opcion == 6:
        print("Usted está saliendo de la base de datos. Hasta pronto.")
    else:
        print("La opción ingresada es incorrecta")             
        
#Aspectos a mejorar: Ingreso de clientes, muestra de datos, pedido de eliminacion de datos