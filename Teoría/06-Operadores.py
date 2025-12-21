#Operadores aritméticos

a=5
b=3

print(a+b) #suma
print(a-b) #resta
print(a*b) #multiplicacion
print(round(a/b,2)) #división
print(a%b) #modulo (resto de la división)
print(a**b)

#Operaciones lógicas

print(a==b) 
print(a!=b)
print(a<b)
print(a<=b)
print(a>b)
print(a>=b)

#Operaciones relacionales

print(a and b) #en este caso, como son distintos, toma como valor la ultima variable
print(a or b)
print(a>(not b))

#Operadores de asignación
c=4
d=5
e=6
f=7

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
