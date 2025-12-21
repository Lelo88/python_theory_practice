#importamos las funciones del archivo modulos (no esta con un numero porque no me deja importarlo)

#from modulos import suma 

#tambien puedo importar de manera general

from modulos import suma, resta, Persona
from moduloscarp import modulos2

print(suma(4,5))
print(resta(10,6))
persona1 = Persona("Leandro", "Villalba",34)
print(persona1.saludo())

#tambien puedo poner el archivo en una carpeta y llamarlo en esta forma: 
# from carpeta import archivo

#luego puedo llamarlo por archivo.funcion // archivo.clase 

auto = modulos2.Vehiculo("Mercedes Benz", "A1", 2020) #se ubica en la carpeta de modulos

print(auto.llamaVehiculo())

