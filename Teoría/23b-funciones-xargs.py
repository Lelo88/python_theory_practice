# en el caso de que quiera utilizar una misma funcion pasando una cierta cantidad de parametros distintos
# las veces que lo llame, puedo realizarlo a traves de xargs

def suma (*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)
    
suma (2,4,5)
suma (1,2)
suma (4,5,6,7,8,9,10)    