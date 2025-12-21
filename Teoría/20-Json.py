
import json #importo la libreria json

data ={}# declaramos un diccionario vacío

data["clients"] = [] 
data["location"] = []

data['clients'].append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17})

data['clients'].append({
    'first_name': 'Joe',
    'last_name': 'Hinners',
    'age': 31,
    'amount': [1.90, 5.50]})

data['clients'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36,
    'amount': 1.11})

print(data)

with open("Teoría/primerJson.json", 'w', encoding ='utf-8') as file: #creo un archivo .json con los datos agregados anteriormente dentro de la carpeta teoria 
    json.dump(data, file, indent=4) #crear el contenido del archivo json con la variable, el tipo de archivo y el identado del contenido
