buscar_palabra = input("Palabra a buscar: ")

num_linea = 0 #Contador de línea que se incrementa en cada vuelta del for

encontrado = False #Booleano que arranca en False (la "bandera")

with open("tareas.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        num_linea += 1

        if buscar_palabra.lower() in linea.lower(): #Para que "ir" encuentre "Ir"
           print (f"Línea {num_linea}: {linea.strip()}")
           encontrado = True #Pasa a True cuando encuentra algo

if not encontrado:
    print(f'No hay ninguna línea con "{buscar_palabra}".')