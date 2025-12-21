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
    
    def __str__(self):
        return f'Soy un perro de raza {self.raza} y tengo {self.edad}' 
    
class Persona():
    
    def __init__(self, nombre, apellido, edad, meta, perro):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.meta = meta
        self.perro = perro
        
    def saluda (self):
        return f'hola, me llamo {self.nombre} {self.apellido} y tengo {self.edad} años'
    
    def camina(self, pasos):
        if pasos>=self.meta:
            return f'Felicidades {self.nombre}. Cumpliste tu meta diaria'
        else:
            return 'No lograste tus metas. Ponete las pilas'
        
perro1 = Perro(nombre="Pedro", raza = "caniche", edad = 2)
perro2 = Perro("Pepito","cocker",3)

#Ahora le paso como variable a las instancias que voy a crear de persona las instancias de perro

persona1 = Persona("Lionel","Messi",35,4500,perro1)
persona2 = Persona("Cristiano","Ronaldo",37,5000,perro2)

print(persona1.perro)   #Si no defino el metodo especial __str__, me imprimira la ubicacion en memoria
                        #Para eso lo defino en la clase perro
print(persona2.perro)