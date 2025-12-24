# Reto 3: Receta de cocina

def pedir_texto(prompt):
    while True:
        valor = input(prompt).strip()
        if valor:
            return valor
        print("El valor no puede estar vacio.")

def pedir_ingredientes():
    while True:
        crudos = input("Ingredientes (separados por comas): ").strip()
        items = [ing.strip() for ing in crudos.split(",") if ing.strip()]
        if items:
            return items
        print("Introduce al menos un ingrediente.")

def pedir_entero_positivo(prompt):
    while True:
        valor = input(prompt).strip()
        try:
            numero = int(valor)
            if numero > 0:
                return numero
            print("Debe ser un numero entero mayor que cero.")
        except ValueError:
            print("Introduce un numero entero valido.")

def pedir_dificultad():
    opciones = {"facil": "Facil", "media": "Media", "alta": "Alta"}
    while True:
        valor = input("Dificultad (Facil, Media, Alta): ").strip().lower()
        if valor in opciones:
            return opciones[valor]
        print("Opcion no valida. Usa: Facil, Media o Alta.")

def main():
    print("=== Registro de Receta ===")
    nombre = pedir_texto("Nombre de la receta: ")
    ingredientes = pedir_ingredientes()
    tiempo = pedir_entero_positivo("Tiempo de preparacion (minutos): ")
    dificultad = pedir_dificultad()

    print("\nResumen:")
    print(f"  Receta: {nombre}")
    print(f"  Ingredientes: {', '.join(ingredientes)}")
    print(f"  Tiempo: {tiempo} minutos")
    print(f"  Dificultad: {dificultad}")

if __name__ == "__main__":
    main()
