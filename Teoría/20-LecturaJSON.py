import json

with open("Teoría/primerJson.json", encoding = "utf-8") as file: #abro el archivo. si tengo que leer, lo hago de manera predeterminada

    dataLectura = json.load(file) #variable donde cargo el archivo json. Es una variable tipo diccionario

    for client in dataLectura['clients']: #recorro el archivo json
        print('First name:', client['first_name'])
        print('Last name:', client['last_name'])
        print('Age:', client['age'])
        print('Amount:', client['amount'])
        print('')