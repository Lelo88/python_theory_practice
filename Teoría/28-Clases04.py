#Encapsulamiento
#Para evitar que un dato no sea editado, lo podemos encapsular para que no pierda su valor. 
#Queda oculto para ser accedido, 

class Persona():
    
    def __init__(self, nombre, apellido, edad, meta):
        self.nombre = nombre
        self.apellido = apellido
        self.__edad = edad
        self.__meta = meta

        
    def saluda (self):
        return f'hola, me llamo {self.nombre} {self.apellido} y tengo  años'
    
    def camina(self, pasos):
        if pasos>=self.__meta:
            return f'Felicidades {self.nombre}. Cumpliste tu meta diaria'
        else:
            return 'No lograste tus metas. Ponete las pilas'
        
    def get_meta(self):
        return self.__meta
    
    def set_meta(self, nueva_meta):
        self.__meta = nueva_meta
    
    def obtener_edad(self):
        return self.__edad
    
    def suma_edad(self):
        return self.__edad + 1 
        
persona1 = Persona("Lionel","Messi",35,4500)

#print(persona1.__edad) #Esto me da error. Para poder acceder, necesito crear un metodo

print(persona1.obtener_edad())

#persona1.__edad=50 #por mas que reasigne, no puedo editarlo por fuera de la clase, si por dentro

print(persona1.suma_edad()) #Ahora si puedo modificar la edad



#tambien pueden encapsularse metodos

persona1.set_meta(150000)

print(persona1.get_meta())
