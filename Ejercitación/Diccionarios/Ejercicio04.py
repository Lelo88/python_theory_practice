#Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla 
# la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

meses = {1:'Enero',2:'Febrero',3:'Marzo',4:'Abril',5:'Mayo',
        6:'Junio',7:'Julio',8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre',12:'Diciembre'}

fecha = input("Ingrese una fecha en formato dd/mm/aaaa").split('/')
#La funcion split la uso para separar en elementos de listado 

print(f'La fecha ingresada es {fecha[0]} de {meses[int(fecha[1])]} de {fecha[2]}')
#Pongo int porque las claves se encuentran en int
