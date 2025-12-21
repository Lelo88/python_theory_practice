
num1 = int(input("Ingrese un número: "))
lim1 = int(input("Ingrese un número que sea el límite inferior: "))
lim2 = int(input("Ingrese un número que sea el límite superior: "))

def recortar(n, inf, sup):
    
    if n>sup:
        return sup
    elif n<inf:
        return inf
    else: 
        return n 
    
print(recortar(num1,lim1,lim2))