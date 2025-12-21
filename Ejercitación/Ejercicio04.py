
year = input("Ingrese un año: ") #realizo el ingreso del año

def año_bisiesto(ye): #defino la funcion año_bisiesto, pidiendo un parametro que va a ser lo que ingresemo
    while not (ye.isnumeric()):  #mientras lo que ingrese no sea un caracter numerico, lo vuelvo a pedir
        ye = (input("Ingrese un año de manera correcta: "))
    
    ye=int(ye) #realizo el parseo a entero para corroborar si el año es bisiesto
    if ye%4 == 0:
        if ye%100!=0:
            return 'El año es bisiesto' #si el año es divisible por 4 pero no por 100, es bisiesto
        elif ye % 400 == 0:
            return 'El año es bisiesto' #si el año es divisible por 4 y por 400, es bisiesto
        else:
            return 'El año no es bisiesto' #si el año es divisible por 100 pero no por 400, no es bisiesto
    else:
        return 'El año no es bisiesto' #si el año no es divisible por 4, no es bisiesto

print(año_bisiesto(year)) #llamo a la funcion dentro de un print para mostrar el retorno

