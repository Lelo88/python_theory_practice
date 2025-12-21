#Escribí un programa que le solicite al usuario ingresar una fecha formada por 8 números, 
# donde los primeros dos representan el día, los siguientes dos el mes y los últimos cuatro 
# el año (DDMMAAAA). Este dato debe guardarse en una variable con tipo int (número entero). 
# Finalmente, mostrar al usuario la fecha con el formato DD / MM / AAAA

fecha = int(input("Fecha en formato DDMMAAAA: "))
anio = fecha % 10000
mes = int(((fecha % 1000000) - anio)/10000)
dia = int(((fecha-(mes*1000))-anio)/1000000)
print(f'{dia}/{mes}/{anio}')