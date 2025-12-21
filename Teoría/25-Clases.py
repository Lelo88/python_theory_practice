class Perro(): # -> Creacion de la clase (por convencion el nombre de la clase tiene que ir en mayuscula)
    
    #Atributos de clase
    patas=4 #tambien defino atributos dentro de la clase
    
    #Atributos de instancia
    def __init__(self, nombre, raza, edad): # -> Metodo constructor de la clase. Siempre deben recibir self
        self.nombre = nombre # self se referira siempre al objeto de la clase que se crea
        self.raza = raza    #nombre, raza y edad son atributos de la clase Perro
        self.edad = edad    #atributos referidos a la instancia de Perro
        
    def ladrar(self): #-> metodos de la clase. le daran funcionalidad al objeto
        return "guau "
        
perro1 = Perro("Pedro","cocker",5)

print(perro1.nombre) # -> Con el punto accedemos a la variable
print(perro1.ladrar()*5)
print(perro1.patas)

class Persona():
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self): #metodo espacial que retornara lo que le pasemos como argumento en la mencion de la clase
        return f'Hola, mi nombre es {self.nombre} {self.apellido}'

    def __len__(self): # devuelve el tamaño de los valores instanciados
        return len(self.apellido + self.nombre)


persona1 = Persona("Leandro","Villalba",34)

print(persona1) #si no le pongo nada, lo que me devolvera es el __str__
print(len(persona1))

class Vector():
    def __init__(self, data):
        self._data = data

    def __str__(self):
        return f'El valor del vector es de {self._data}'

    def __len__(self):
        return len(self._data)

    def __getitem__(self, pos): #este metodo sirve solo para leer, complementandose con setitem
        return self._data[pos]

    def __setitem__(self, pos, value): #setea el valor, tomando como paramentro el valor de la linea 57
        self._data[pos] = value

    def __iter__(self):
        for pos in range(0,len(self._data)):
            yield f'Valor{pos}: {self._data[pos]}'

print("---------------------------")

v = Vector([1,2]) #nosotros interpretamos que esto es una lista, pero Python no, por eso le pasamos las instrucciones para que entienda 
print(f'antes: {v}') #[1,2]
v[1] = 20
print(f'ahora: {v}') #[1,20]

print("\n")
for vec in v:
    print(vec)

#lo que hacen los metodos especiales es interactuar con las instancias de clases, pasando como argumento 
#principal el self