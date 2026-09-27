with open("notas.txt", "w", encoding="utf-8") as archivo: #Abrimos en modo escritura ("w") para crear y cargar el archivo
    while True:
        frase = input("Ingrese una frase (Enter vacío para terminar): ")

        if frase == " ":
            break                      # línea vacía => fin de la carga
           
        # write() escribe EXACTAMENTE la cadena: el '\n' lo ponemos nosotros, si no todas las frases quedan en una sola línea
        archivo.write(frase + "\n")

# Al salir del with el archivo ya está cerrado y guardado en disco
print("Contenido de notas.txt")
with open("notas.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())