#Agregamos un archivo txt en la carpeta para poder leerlo desde este archivo python

archivo = open("Teoría/paraLeer.txt","r",encoding="utf-8") #abro un archivo
print(archivo.read()) #imprime el archivo de texto por consola
archivo.close()#cierro el archivo