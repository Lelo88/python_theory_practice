ciudades = [

    {"id": 1, "city": "Buenos Aires", "country": "Argentina"},

    {"id": 2, "city": "Puerto Quijarro", "country": "Bolivia"},

    {"id": 3, "city": "Mistrató", "country": "Colombia"},

    {"id": 4, "city": "Ouro Branco", "country": "Brazil"},

    {"id": 5, "city": "Ancahuasi", "country": "Peru"},

    {"id": 6, "city": "Cartagena", "country": "Colombia"},

    {"id": 7, "city": "Maras", "country": "Peru"},

    {"id": 8, "city": "Peñaflor", "country": "Chile"},

    {"id": 9, "city": "Pilcaniyeu", "country": "Argentina"},

    {"id": 10, "city": "Abreu e Lima", "country": "Brazil"},

    {"id": 11, "city": "Mucuri", "country": "Brazil"},

    {"id": 12, "city": "Iberia", "country": "Peru"},

    {"id": 13, "city": "San Francisco", "country": "Mexico"},

    {"id": 14, "city": "Pocohuanca", "country": "Peru"},

    {"id": 15, "city": "Chapadinha", "country": "Brazil"},

    {"id": 16, "city": "La Victoria", "country": "Colombia"},

    {"id": 17, "city": "Hacienda La Calera", "country": "Chile"},

    {"id": 18, "city": "Corumbá", "country": "Brazil"},

    {"id": 19, "city": "Corral", "country": "Chile"},

    {"id": 20, "city": "Sucre", "country": "Ecuador"},

    {"id": 21, "city": "Aipe", "country": "Colombia"},

    {"id": 22, "city": "Cauday", "country": "Peru"},

    {"id": 23, "city": "Ipu", "country": "Brazil"},

    {"id": 24, "city": "Marcabal", "country": "Peru"},

    {"id": 25, "city": "Tamandaré", "country": "Brazil"},

    {"id": 26, "city": "San Miguel de Cauri", "country": "Peru"},

    {"id": 27, "city": "Francisco I Madero", "country": "Mexico"},

    {"id": 28, "city": "Tigre", "country": "Argentina"},

    {"id": 29, "city": "Emiliano Zapata", "country": "Mexico"},

    {"id": 30, "city": "Tambo", "country": "Peru"},

    {"id": 31, "city": "Ventanas", "country": "Ecuador"},

    {"id": 32, "city": "Oriximiná", "country": "Brazil"},

    {"id": 33, "city": "Miguel Pereira", "country": "Brazil"},

    {"id": 34, "city": "Pinheiro", "country": "Brazil"},

    {"id": 35, "city": "Espinal", "country": "Colombia"},

    {"id": 36, "city": "Pucacaca", "country": "Peru"},

    {"id": 37, "city": "Otuzco", "country": "Peru"},

    {"id": 38, "city": "Francisco J Mujica", "country": "Mexico"},

    {"id": 39, "city": "Taboão da Serra", "country": "Brazil"},

    {"id": 40, "city": "Cayna", "country": "Peru"},

    {"id": 41, "city": "Riberalta", "country": "Bolivia"},

    {"id": 42, "city": "El Aguacate", "country": "Mexico"},

    {"id": 43, "city": "San Andrés Villa Seca", "country": "Guatemala"},

    {"id": 44, "city": "Paty do Alferes", "country": "Brazil"},

    {"id": 45, "city": "Nova Odessa", "country": "Brazil"},

    {"id": 46, "city": "María la Baja", "country": "Colombia"},

    {"id": 47, "city": "El Retorno", "country": "Colombia"},

    {"id": 48, "city": "Granada", "country": "Colombia"},

    {"id": 49, "city": "Crateús", "country": "Brazil"},

    {"id": 50, "city": "Yanahuanca", "country": "Peru"}

]

capitales = [("Bolivia", "Sucre"), ("Peru", "Lima"), ("Argentina", "Buenos Aires"),
            ("Chile", "Santiago"), ("Brazil", "Brasilia"), ("Colombia", "Bogotá"),
            ("Mexico", "Mexico DF"), ("Guatemala", "Ciudad de Guatemala"), ("Ecuador", "Quito")]

paises = []
for pais in ciudades:
    if pais["country"] not in paises:
        paises.append(pais["country"])

print(tuple(paises)) 