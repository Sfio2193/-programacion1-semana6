ARCHIVO_COMPRAS = "compras.txt"

def mostrar_lista():
    print("Lista actual")
    cantidad = 0
    with open(ARCHIVO_COMPRAS, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if linea.strip() != "":
                cantidad = cantidad + 1
                print(f"{cantidad}. {linea.strip()}")
    return cantidad

def agregar_item(item):
    with open(ARCHIVO_COMPRAS, "a", encoding="utf-8") as archivo:
        archivo.write(item + "\n")

def ej_integrador():
    print("Lista de compras — Programación I")
    with open(ARCHIVO_COMPRAS, "w", encoding="utf-8") as archivo:
        for i in range(1, 4):
            item = input(f"Ítem {i}: ")
            archivo.write(item + "\n")

    total = mostrar_lista()
    respuesta = input("¿Desea agregar otro ítem? (s/n): ").strip().lower()
    while respuesta == "s":
        nuevo = input("Nuevo ítem: ")
        agregar_item(nuevo)
        total = mostrar_lista()
        respuesta = input("¿Desea agregar otro ítem? (s/n): ").strip().lower()
    print(f"Lista guardada con {total} ítems. ¡Hasta la próxima compra!")

ej_integrador()

# Para que no borre las compras de los días anteriores al volver a abrir el programa, tendríamos que cambiar el modo de 
# la carga de los 3 primeros ítems de "w" a "a".