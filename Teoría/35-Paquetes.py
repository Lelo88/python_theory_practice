from setuptools import setup

setup(
    name="mi_primer_paquete",
    version = "1.0", #cuantos mas numeros hay a la derecha, los cambios que se presentan son menos trascendentales
    description = "Estamos creando el primer paquete distribuido",
    author = "Clase Coder Python",
    author_email="coder@coder.com",

    package = ["mi_paq"] #aca va la carpeta que vamos a transformar como paquete
    #usando sdist se crea un comprimible con lo que contiene 35-Paquetes.py
)

#utilizamos estos datos para realizar versiones distribuidas de nuestro paquete