#Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se
#almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el
#coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura,
#pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número
#de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará
# por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe
# mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

import os

detalleFacturas = {}

opcion,cobrado,pendiente = 0,0,0

while opcion!=4:
    print("--------------MENU DE FACTURACION------------")
    print("1- Ingreso de facturas")
    print("2- Listado de facturas a pagar")
    print("3- Pago de facturas")
    print("4- Salir del programa de facturación")
    
    print(f'\nPendiente al momento: {pendiente}')
    print(f'Cobrado al momento: {cobrado}')
    opcion=int(input("\n Ingrese una opción: "))
    os.system("cls")
    if opcion == 1: 
        facturas = input("Ingrese las facturas que tiene pendientes a pagar con el formato DETALLE:PAGO : ")
        for detalle in facturas.split(','):
            detal,valor = detalle.split(':')
            detalleFacturas[detal] = float(round(valor,2))
            pendiente +=detalleFacturas[detal]
        os.system("pause")
        os.system("cls")
    elif opcion == 2:
        print(f'Cantidad de facturas: {len(detalleFacturas)}')
        for detalle, precio in detalleFacturas.items():
            print(f'{detalle}: {precio}')
        os.system("pause")
        os.system("cls")
    elif opcion == 3:
        factura = input("Ingrese la factura que desea pagar: ")
        if factura in detalleFacturas:
            coste = detalleFacturas.pop(factura,0)
            cobrado+=coste
            pendiente-=coste
            os.system("pause")
            os.system("cls")
        else:
            print("La factura que desea eliminar no existe en la base de datos")
            os.system("pause")
            os.system("cls")
    elif opcion==4:
        print("Usted está saliendo del programa de facturación. Hasta pronto!")
    else:
        opcion = int(input("La opción ingresada es incorrecta. Ingrese otra opción: "))
