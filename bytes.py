# Modo texto: Python DECODIFICA los bytes con UTF-8 y nos da un str.
with open("tareas.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read()

# Modo binario ("rb"): nos da los bytes crudos, sin decodificar.
with open("tareas.txt", "rb") as archivo:
    datos = archivo.read()
print(f"Caracteres: {len(texto)} - Bytes: {len(datos)}")
print(type(texto), type(datos))
print(datos)

# Los largos difieren en exactamente 1: la "é" de "médico" es UN
# carácter pero ocupa DOS bytes en UTF-8 (\xc3\xa9). Todo el resto del
# archivo es ASCII puro: un byte por carácter.
# (Si el archivo no termina en \n, los números dan 67 y 68.)
# Extra: texto.encode("utf-8") == datos  -> True: codificar el str
# da exactamente los bytes del disco.


ancho, alto = 3, 2
# Los 6 píxeles, de izquierda a derecha y de arriba hacia abajo.
pixeles = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),        # rojo, verde, azul
    (255, 255, 0), (255, 255, 255), (0, 0, 0),    # amarillo, blanco, negro
]
# "wb": escritura binaria. write() acepta bytes, NO str.
with open("imagen.ppm", "wb") as archivo:
    # El encabezado es texto ASCII: lo convertimos con encode().
    archivo.write(f"P6 {ancho} {alto} 255\n".encode("ascii"))
    for (r, g, b) in pixeles:
        # bytes([...]) arma 3 bytes a partir de 3 enteros de 0 a 255.
        archivo.write(bytes([r, g, b]))
import os
print("imagen.ppm generado:", os.path.getsize("imagen.ppm"), "bytes")
# 11 bytes de encabezado ("P6 3 2 255\n") + 6 píxeles x 3 bytes = 29.