#Operadores aritméticos

a=5
b=3

# operaciones aritméticas
print(a+b) #suma
print(a-b) #resta
print(a*b) #multiplicacion
print(round(a/b,2)) #división
print(a%b) #modulo (resto de la división)
print(a**b)

#Operaciones relacionales

print(a==b) 
print(a!=b)
print(a<b)
print(a<=b)
print(a>b)
print(a>=b)

#Operaciones lógicos

print(a and b) #en este caso, como son distintos, toma como valor la ultima variable
print(a or b)
print(a>(not b))

#Operadores de asignación

c=4
d=5
e=6
f=7

# operadores de asignación compuestos
c += 3  #c = c + 3 
print(c)
d -= 5
print(d)
e *= 2
print(e)
f /=2
print(f)

#Tambien se puede operar sobre strings

nombre1 = "Leandro"
nombre2 = "Romina"

print(nombre1<nombre2) #es true porque R en ASCII tiene el valor mas grande que L
print(nombre1>nombre2) #false
print(nombre1 or nombre2)

# asignación de valores múltiples
x,y,z = 1,2,3
print(x,y,z)

# asignación de valores múltiples por input
x,y,z = input("Ingrese tres números separados por comas: ").split(",")
print(x,y,z)
