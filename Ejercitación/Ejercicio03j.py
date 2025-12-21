#6) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan 
# en ellas, pero no debe repetirse ningún elemento en la nueva lista:

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

repetidos = []

for letra in lista_1:
    for letra2 in lista_2:
        if letra==letra2:
            if (letra not in repetidos):
                repetidos.append(letra)

print(repetidos)