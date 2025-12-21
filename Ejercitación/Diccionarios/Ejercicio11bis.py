#Lo mismo que el ejercicio 11, pero ahora practicando un poco con funciones 

import os
from random import randint

socio = {}

def menu():
    opcion = 0
    while opcion!=3:
        os.system("cls")
        print("MENU DE SOCIOS\n")
        print("1-Ingreso de socios")
        print("2-Visualización de socios")
        print("3-Salir del menú")
        opcion= int(input("\n Elija una opción: "))

        os.system("cls")
        
        if opcion == 1:
            ingresoDatos()
        elif opcion == 2:
            verDatos()
        elif opcion == 3:
            print("Usted está saliendo del programa. Hasta pronto. ") 
        else:
            print("")

def ingresoDatos():
    print("INGRESO DE DATOS")
    dni = int(input("DNI: "))
    datosSocio = {}
    while dni!=0:
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = int(input("Edad: "))
        socioNum = randint(0,1000)
        datosSocio = {"nombre":nombre, "apellido": apellido, "edad":edad, "numSocio": socioNum}
        socio[dni] = datosSocio
        datosSocio = len(datosSocio) + 1
        dni = int(input("DNI: "))
    os.system("pause")

def verDatos():
    print("VISUALIZACION DE DATOS\n")
    for idDni,valor in socio.items():
        print(f'{idDni}: {valor["numSocio"]} {valor["nombre"]} {valor["apellido"]} {valor["edad"]}')
    os.system("pause")

if __name__=="__main__":
    menu()
