import os   # solo para ver si un archivo existe y cuánto pesa
print("Experimento 1: abrir inexistente.txt con 'r'")
try:
    with open("inexistente.txt", "r", encoding="utf-8") as archivo:
        pass
except FileNotFoundError as error:
    # Resultado: FileNotFoundError. "r" exige que el archivo exista.
    print("   -> Error:", type(error).__name__, "-", error)

print("Experimento 2: abrir inexistente.txt con 'a' sin escribir nada")
with open("inexistente.txt", "a", encoding="utf-8") as archivo:
    pass
    # Resultado: el archivo APARECE en la carpeta, con 0 bytes. Abrir en
    # modo "a" (o "w") crea el archivo aunque no se escriba nada.
print("   -> ¿existe?", os.path.exists("inexistente.txt"),
    "| tamaño:", os.path.getsize("inexistente.txt"), "bytes")
os.remove("inexistente.txt")      # limpiamos para dejar todo como estaba

print("Experimento 3: abrir tareas.txt con 'r' e intentar write()")
try:
    with open("tareas.txt", "r", encoding="utf-8") as archivo:
            archivo.write("hola")
except OSError as error:
    # Resultado: io.UnsupportedOperation: not writable.
    # El modo "r" es SOLO lectura: el archivo no se modifica.
    print("   -> Error:", type(error).__name__, "-", error)

print("Experimento 4: 'w+', escribir, seek(0) y leer")
with open("copia.txt", "w+", encoding="utf-8") as archivo:
    archivo.write("Una línea de prueba\n")
    print("   -> posición después de escribir:", archivo.tell())
    archivo.seek(0)               # volver al byte 0
    print("   -> posición después de seek(0):", archivo.tell())
    print("   -> read() devuelve:", repr(archivo.read()))

print("Experimento 4 bis: lo mismo SIN seek(0)")
with open("copia.txt", "w+", encoding="utf-8") as archivo:
    archivo.write("Una línea de prueba\n")
    print("   -> read() devuelve:", repr(archivo.read()))
    # Resultado: '' (cadena vacía). Después de escribir, el cursor quedó
    # al FINAL, y read() lee "desde acá hasta el final": nada.
os.remove("copia.txt")