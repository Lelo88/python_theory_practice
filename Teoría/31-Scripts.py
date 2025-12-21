#paso de argumentos a un script
import sys

print(sys.argv) # paso de parametros por la terminal 

print("Hola mundo")

print(f'Hola {sys.argv[1]} el año que viene vas a tener {int(sys.argv[2]) + 1}') #asumiento que le pasamos strings que correspondan

# pasamos al ejemplo de pasar dos strings y un listado (aunque la terminal lo toma como string tambien)

ciudades = sys.argv[3].strip('][').split(',')

print(ciudades)   #['Buenos Aires', ' La Pampa', ' Entre Rios']

for ciudad in ciudades: 
    print(f'{sys.argv[1]} visitó {ciudad.strip()}')
    