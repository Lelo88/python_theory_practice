#Descripción de la actividad. Escribir un programa que indique la generación correspondiente para un año de nacimiento 
# indicado. 
# Trabajarán con el notebook de clase Clase_4.ipynb
# Importante: Para los años que no pertenezcan a ninguna generación, se deberá colocar: 
# “No existe generación asociada”

año = int(input("Ingrese el año de su nacimiento: "))

if(año>=1920 and año<=1940):
    print("Pertenecés a la generación silenciosa")
elif(año>=1946 and año<=1964):
    print("Pertenecés a la generación Baby Boomer")
elif(año>=1965 and año<=1979):
    print("Pertenecés a la generación X")
elif(año>=1980 and año<=2000):
    print("Pertenecés a la generación Y")
elif(año>=2001 and año<=2010):
    print("Pertenecés a la generación Z")
else:
    print("No pertenecés a ninfuna generación!")    