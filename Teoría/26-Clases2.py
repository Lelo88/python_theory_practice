class Persona():
    
    def __init__(self, nombre, apellido, edad, meta):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.meta = meta
        
    def saluda (self):
        return f'hola, me llamo {self.nombre} {self.apellido} y tengo {self.edad} años'
    
    def camina(self, pasos):
        if pasos>=self.meta:
            return f'Felicidades {self.nombre}. Cumpliste tu meta diaria'
        else:
            return 'No lograste tus metas. Ponete las pilas'
        
persona1=Persona('Lionel','Messi',35,5000)
persona2=Persona('Cristiano','Ronaldo',37,4000)

print(persona1.camina(4500))
print(persona2.camina(4500))

