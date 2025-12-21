#Voy a replicar un ejercicio de introduccion al desarrollo de software de la facultad

#Utilizando datos tipo struct, estructuras de control de flujo switch case y funciones,
#escriba un algoritmo que permita cargar los socios de un club (máximo 100 socios). 
#  La información de cada socio será: nombre, apellido, no documento, fecha de
#nacimiento, edad (la cual se debe calcular automáticamente a partir de la fecha de
#nacimiento, se puede ayudar con time.h), y un número de socio (distinto al DNI)
#generado automáticamente.  La interfaz de programa debe ser a través de un menú, donde el usuario pueda
#elegir entre ingresar datos, ver los datos cargados, o salir del programa.  Al estar en la etapa de ingreso de datos, se debe solicitar de manera secuencial
#cada uno de los datos de cada socio. Es decir, para el primer socio solicitar cada
#uno de los datos mencionados, luego pasar al segundo socio, etc., hasta que el
#usuario decida finalizar la carga ingresando un DNI negativo.  Al finalizar la carga se debe regresar al menú principal, y desde ahí el usuario
#debe poder elegir si desea ingresar más socios, ver los socios ya cargados, o salir
#del programa.

import os
from random import randint


socios = {}
opcion = 0
titulo = "Menú de ingreso de socios"
while opcion!=3: 
    
    os.system("cls")
    
    print(titulo.center(130))
    print("1-Ingreso de socios")
    print("2-Visualización de socios")
    print("3-Salir del menú")
    opcion= int(input("\n Elija una opción: "))

    os.system("cls")

    if opcion==1:
        print("INGRESO DE DATOS DE SOCIOS\n")
        dni = int(input("DNI: "))
        datosSocio = {}
        while dni!=0:
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = int(input("Edad: "))
            socioNum = randint(0,1000)
            datosSocio = {"nombre":nombre, "apellido": apellido, "edad":edad, "numSocio": socioNum}
            socios[dni] = datosSocio
            datosSocio = len(datosSocio) + 1
            dni = int(input("DNI: "))
        os.system("pause")
    elif opcion == 2:
        for idDni,valor in socios.items():
            print(f'{idDni}: {valor["numSocio"]} {valor["nombre"]} {valor["apellido"]} {valor["edad"]}')
        os.system("pause")
    elif opcion == 3:
        print("Usted está saliendo del programa de socios. Hasta luego.")
    else: 
        print("")