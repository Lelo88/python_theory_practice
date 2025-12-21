# Desarrollar un programa que permita calcular el promedio final de puntos de los equipos de fútbol 
# en un torneo.
# La cantidad de partidos que debemos considerar a un equipo para el ejemplo se detallan 
# a continuación: partidos_ganados 8 partidos_empatados 7 partidos_perdidos 5

partidos_ganados = int(input("Ingrese la cantidad de partidos ganados: "))
partidos_empatados = int(input("Ingrese la cantidad de partidos empatados: "))
partidos_perdidos =  int(input("Ingrese la cantidad de partidos perdidos: "))

totalPartidos = partidos_ganados + partidos_empatados + partidos_perdidos

totalPuntos = (partidos_ganados * 2) + (partidos_empatados * 1) + (partidos_perdidos * 0)

promedio = totalPuntos / totalPartidos

print("El promedio total de los",totalPartidos,"partidos jugados es de ", promedio)


