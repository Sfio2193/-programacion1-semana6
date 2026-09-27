suma = 0
cantidad = 0
aprobados = []          # lista de cadenas "Nombre (nota)"
with open("notas.csv", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        if linea.strip() == "":
            continue    # saltear líneas vacías
            # strip() ANTES de split(): sin él, la nota llegaría como "8\n".
            # split(";") devuelve ["Ana", "8"]; el desempaquetado en dos
            # variables es el mismo de las tuplas de la semana pasada.
        nombre, nota = linea.strip().split(";")
        nota = int(nota)            # todo lo que viene de un archivo es str
        suma = suma + nota
        cantidad = cantidad + 1
        if nota >= 6:
            aprobados.append(f"{nombre} ({nota})")
# Mostramos DESPUÉS de leer todo: el promedio necesita el total.
print(f"Promedio general: {suma / cantidad}")
print("Aprobados:")
for alumno in aprobados:
    print(f"  {alumno}")