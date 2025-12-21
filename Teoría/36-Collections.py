from collections import namedtuple, Counter

Fish = namedtuple("Fish",["name", "species", "tank"])

miPrimerPez = Fish("Sammy", "Tiburon", "Tanque") #Fish es una clase

print(miPrimerPez) #Fish(name='Sammy', species='Tiburon', tank='Tanque')

print(miPrimerPez._asdict()) #{'name': 'Sammy', 'species': 'Tiburon', 'tank': 'Tanque'}

l = [1,2,3,4,1,2,3,1,2,1]
print(Counter(l)) #diccionario con key y values que representan los valores y la cantidad de veces que se repiten

estudiantes = "Nicolás Claudio Brenda Flor Nicolás Flor"

print(Counter(estudiantes)) #contara la cantidad de veces que se repiten las letras

print(Counter(estudiantes.split())) #contara la cantidad de veces que se repiten los nombres (gracias a split)

#Counter({'o': 5, 'l': 5, ' ': 5, 'i': 3, 'r': 3, 'N': 2, 'c': 2, 'á': 2, 's': 2, 'a': 2, 'd': 2, 'F': 2, 'C': 1, 'u': 1, 'B': 1, 'e': 1, 'n': 1})
#Counter({'Nicolás': 2, 'Flor': 2, 'Claudio': 1, 'Brenda': 1})