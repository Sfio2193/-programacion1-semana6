suma = 0
cantidad = 0
# Dos with anidados: uno lee notas.csv y el otro escribe resultados.txt.
# (Alternativa igual de válida: leer todo a una lista y escribir después.)
with open("notas.csv", "r", encoding="utf-8") as entrada:
    with open("resultados.txt", "w", encoding="utf-8") as salida:
        for linea in entrada:
            if linea.strip() == "":
                continue
            nombre, nota = linea.strip().split(";")
            nota = int(nota)
            suma = suma + nota
            cantidad = cantidad + 1
            if nota >= 6:
                estado = "Aprobado"
            else:
                estado = "Desaprobado"
            renglon = f"{nombre} - {nota} - {estado}"
            print(renglon)                    # por pantalla...
            salida.write(renglon + "\n")      # ...y al archivo (con \n)
        promedio = suma / cantidad
        print(f"Promedio general: {promedio}")
        salida.write(f"Promedio general: {promedio}\n")
print("Archivo resultados.txt generado. Verificación:")
with open("resultados.txt", "r", encoding="utf-8") as verificacion:
    for linea in verificacion:
        print(linea.strip())