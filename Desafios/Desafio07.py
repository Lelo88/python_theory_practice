#Descripción de la actividad. 
# Para aprobar un crédito, el cliente debe ser mayor de edad. Además, 
# debe tener una antigüedad en el sistema financiero de mínimo 3 años y un ingreso mayor a 2500 dólares.  
# En caso no tenga la antigüedad suficiente, su ingreso mensual debe ser como mínimo 4000 dólares. Si no cumple ninguna de las condiciones, no se aprueba el crédito
# Datos iniciales
# edad = 15
# antigüedad = 10
# ingreso = 1500

edad = int(input("Ingrese su edad: "))
antiguedad = int(input("Ingrese su antiguedad en el banco: "))
ingreso = int(input("Ingrese su salario mensual: "))

if(edad>18 and antiguedad >= 3 and ingreso>=2500):
    print("Credito aprobado")
elif(antiguedad<3 and ingreso>=4000):
    print("Credito aprobado")
else:
    print("Credito desaprobado")
    