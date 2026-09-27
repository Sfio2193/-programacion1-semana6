with open("notas.txt", "a", encoding="utf-8") as archivo: #Abrimos en modo APPEND ("a") para agregar al final sin borrar nada
    while True:
        frase = input("Ingrese una frase (Enter vacío para terminar): ")
        if frase == " ":
           break                     
        archivo.write(frase + "\n")


print("Contenido de notas.txt")
with open("notas.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())


#El modo "w" (Write) borra por completo el contenido del archivo antes de escribir, creando uno nuevo desde cero.
#El modo "a" (Append) conserva los datos existentes y posiciona el puntero al final para agregar la nueva información.
#Usaría "w" para inicializar o sobrescribir una configuración, y "a" para registrar historiales o listas acumulativas.