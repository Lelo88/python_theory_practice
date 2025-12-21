#los metodos que utilizamos a lo largo del curso son funciones propias del lenguaje python
#como programadores, somos capaces de crear nuestras propias funciones 

#para eso las funciones propias las definimos con def

#def nombrefuncion(parametros)
#    sentencias --> bloque de codigo
#    return (expresion) --> devolucion de la funcion

def saludar():
    print("Estoy saludando desde la funcion")
    
saludar() #--> llamado de la funcion 

#paso de parametros a una funcion
nombre = "Leandro"
def saludar_con_nombre(nom):
    saludando = print(f'Hola {nom} como estas?')
    return saludando    

saludar_con_nombre(nombre)

#las variables que se definen DENTRO de una funcion solo existen dentro de la misma
#al usar variables globales puedo reutilizarlas dentro de la funcion, pero puede que me devuelva un valor distinto:

numero = 5
def suma():
    print(f'{numero+10}')
    
suma()    #numero ahora vale 15

