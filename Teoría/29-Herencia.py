class Persona():

    def __init__(self, nombre, apellido, edad, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni

    def saluda(self):
        return f'Hola, me llamo {self.nombre}{self.apellido} y tengo {self.edad} años'

class Empleado(Persona): #1. La clase empleado hereda los atributos y funcionalidades de la clase Persona

    def __init__(self, nombre, apellido, edad, dni, sueldo, horario):
        super().__init__(nombre, apellido, edad, dni) #trasmision de los atributos de Persona a Empleado
        self.sueldo = sueldo
        self.horario = horario

    def saluda(self): #3. y tambien sobreescribir los metodos (polimorfismo)
        return (f'{super().saluda()}' f' y gano {self.sueldo} dolares')

    def fichar(self, ingreso): #2. pueden tener sus propios metodos
        if(ingreso <= self.horario):
            return f'LLegué {self.horario - ingreso} min temprano'
        else:
            return f'LLegué {ingreso - self.horario} min tarde'

class Seguridad(Empleado): #4. La clase Seguridad hereda los atributos y metoods de Empleado y Persona

    def __init__(self, nombre, apellido, edad, dni, sueldo, horario, vehiculo, arma):
        super().__init__(nombre, apellido, edad, dni, sueldo, horario)
        self.vehiculo = vehiculo
        self.arma = arma

    def llamar_policia(self, mensaje):
        return f'Hola policía, les quiero decir que {mensaje}'

persona1 = Persona("Mauricio", "Cuello", 31, 6565058) 

empleado1 = Empleado("Pepe", "Argento", 55, 3024657, 1500, 360)

seguridad1 = Seguridad("Lionel", "Messi", 35, 1236579, 1200, 300, "fiat 600", "AK-47")

print(persona1.saluda()) #Tendra el saludo definido en Persona
print(empleado1.saluda())
print(seguridad1.saluda()) #Tendra el saluda de empleado porque el orden de funciones va
                            #desde la ultima clase hija hasta la clase padre, en este cas, de Empleado