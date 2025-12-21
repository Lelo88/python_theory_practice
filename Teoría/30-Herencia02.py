class Mamifero():

    def __init__(self, cant_mamas, esp_vida):
        self.cant_mamas = cant_mamas
        self.esp_vida = esp_vida
        self.peso = 0.5
        self.__vivo = False

    def mamar(self, tiempo):
        self.peso += tiempo * 0.2

    def nacer(self):
        self.__vivo = True

    def esta_vivo(self):
        if (self.__vivo):
            return 'Está vivo'
        else:
            return 'No está vivo'

    def nadar(self):
        return 'Estoy nadando como un mamifero...'

class AnimalMarino():

    def __init__(self, tiene_branqueas, especie):
        self.tiene_branqueas = tiene_branqueas
        self.especie = especie

    def nadar(self):
        return 'Estoy nadando...'

class Cetaceo(Mamifero, AnimalMarino):

    def __init__(self, cant_mamas, esp_vida, tiene_branqueas, especie, notas, vive_en):
        Mamifero.__init__(self, cant_mamas, esp_vida) #Esto funciona como super
        AnimalMarino.__init__(self, tiene_branqueas, especie)  #Esto funciona como super
        self.notas = notas
        self.vive_en = vive_en

    # def nadar(self):

    #     return f'Soy un cetaceo nadando como nada un cetaceo'

# mamifero1 = Mamifero(4, 10)

# print(mamifero1.esta_vivo())

# mamifero1.nacer()

# print(mamifero1.esta_vivo())

cetaceo1= Cetaceo(6, 8, True, "Ballena Azul", "Vive en aguas muy profundas", "Atlantico")
print(cetaceo1.nadar())